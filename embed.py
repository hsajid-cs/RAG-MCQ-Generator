"""Build a simple embedding index for markdown corpus files.

This script performs three steps:
1. Discovers markdown documents inside the corpus directory.
2. Applies sliding-window chunking over tokenised text (word based).
3. Generates sentence-transformer embeddings and stores them on disk.

The resulting index folder contains:
- ``embeddings.npy``: NumPy array of shape (chunks, embedding_dim).
- ``chunks.jsonl``: metadata (document id, offsets, raw text) per chunk.

Run ``python embed.py --help`` for CLI options.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator, List, Sequence

import numpy as np

try:
    from sentence_transformers import SentenceTransformer
except Exception:
    SentenceTransformer = None

_model = None
def _get_model():
    global _model
    if _model is None:
        if SentenceTransformer is None:
            raise RuntimeError("Install sentence-transformers to enable embeddings: pip install sentence-transformers")
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model

def embed_texts(texts: List[str]) -> List[np.ndarray]:
    """Return list/array of embeddings (dtype float)."""
    model = _get_model()
    embs = model.encode(texts, show_progress_bar=False, convert_to_numpy=True)
    return embs


INPUT_DIR = Path("corpus")
OUTPUT_DIR = Path("index")
MODEL = "sentence-transformers/all-MiniLM-L6-v2"
WINDOW_SIZE = 256
WINDOW_STRIDE = 64
BATCH_SIZE = 512


@dataclass
class Chunk:
	"""Container for a chunk of source text."""

	document_id: str
	chunk_id: int
	text: str
	start_word: int
	end_word: int


def iter_markdown_files(root: Path) -> Iterator[Path]:
	"""Yield markdown files relative to the provided root directory."""

	if not root.exists():
		raise FileNotFoundError(f"Input directory not found: {root}")

	yield from root.rglob("*.md")


def normalise_whitespace(text: str) -> str:
	"""Collapse excessive whitespace while preserving paragraph breaks."""

	lines = [line.strip() for line in text.splitlines()]
	# Keep blank lines to preserve some structure for the downstream splitter.
	cleaned: List[str] = []
	previous_blank = False
	for line in lines:
		if not line:
			if not previous_blank:
				cleaned.append("")
			previous_blank = True
		else:
			cleaned.append(line)
			previous_blank = False

	return "\n".join(cleaned).strip()


def sliding_windows(words: Sequence[str], window_size: int, stride: int) -> List[tuple[int, int]]:
	"""Produce (start, end) index pairs using a sliding window over the words list."""

	if not words:
		return []

	if window_size <= 0:
		raise ValueError("window_size must be positive")

	if stride <= 0:
		raise ValueError("stride must be positive")

	if len(words) <= window_size:
		return [(0, len(words))]

	spans: List[tuple[int, int]] = []
	start = 0
	while start < len(words):
		end = min(start + window_size, len(words))
		spans.append((start, end))
		if end == len(words):
			break
		start += stride
	return spans


def chunk_document(path: Path, *, root: Path, window_size: int, stride: int) -> List[Chunk]:
	"""Create sliding-window chunks for a single markdown document."""

	relative_id = path.relative_to(root).as_posix()
	raw_text = path.read_text(encoding="utf-8")
	cleaned = normalise_whitespace(raw_text)
	words = cleaned.split()

	spans = sliding_windows(words, window_size, stride)
	chunks: List[Chunk] = []
	for idx, (start, end) in enumerate(spans):
		# Join on spaces to keep sentence boundaries reasonably intact.
		segment = " ".join(words[start:end])
		chunks.append(
			Chunk(
				document_id=relative_id,
				chunk_id=idx,
				text=segment,
				start_word=start,
				end_word=end,
			)
		)

	return chunks


def embed_chunks(
	chunks: Sequence[Chunk],
	*,
	model_name: str,
	batch_size: int,
	normalize: bool,
) -> np.ndarray:
	"""Encode chunk texts into embeddings using the configured model."""

	model = SentenceTransformer(model_name)

	texts = [chunk.text for chunk in chunks]
	if not texts:
		return np.empty((0, model.get_sentence_embedding_dimension()), dtype=np.float32)

	embeddings = model.encode(
		texts,
		batch_size=batch_size,
		convert_to_numpy=True,
		normalize_embeddings=normalize,
		show_progress_bar=True,
	)

	return embeddings.astype(np.float32, copy=False)


def persist_index(
	*,
	embeddings: np.ndarray,
	chunks: Sequence[Chunk],
	output_dir: Path,
) -> None:
	"""Write embedding matrix and chunk metadata to the output directory."""

	output_dir.mkdir(parents=True, exist_ok=True)

	embeddings_path = output_dir / "embeddings.npy"
	np.save(embeddings_path, embeddings)

	metadata_path = output_dir / "chunks.jsonl"
	with metadata_path.open("w", encoding="utf-8") as handle:
		for chunk, vector in zip(chunks, embeddings):
			record = {
				"document_id": chunk.document_id,
				"chunk_id": chunk.chunk_id,
				"start_word": chunk.start_word,
				"end_word": chunk.end_word,
				"embedding_dim": int(len(vector)),
				"text": chunk.text,
			}
			handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def build_index(
	*,
	input_dir: Path,
	output_dir: Path,
	window_size: int,
	stride: int,
	model_name: str,
	batch_size: int,
	normalize: bool,
) -> None:
	"""End-to-end pipeline for corpus indexing."""

	files = sorted(iter_markdown_files(input_dir))
	if not files:
		print(f"No markdown files found in {input_dir}")
		return

	print(f"Found {len(files)} markdown file(s) under {input_dir}")

	all_chunks: List[Chunk] = []
	for file in files:
		doc_chunks = chunk_document(
			file,
			root=input_dir,
			window_size=window_size,
			stride=stride,
		)
		all_chunks.extend(doc_chunks)
		print(f"  • {file.relative_to(input_dir)} -> {len(doc_chunks)} chunk(s)")

	print(f"Total chunks: {len(all_chunks)}")

	embeddings = embed_chunks(
		all_chunks,
		model_name=model_name,
		batch_size=batch_size,
		normalize=normalize,
	)

	persist_index(embeddings=embeddings, chunks=all_chunks, output_dir=output_dir)

	print(f"Embeddings saved to {output_dir / 'embeddings.npy'}")
	print(f"Metadata saved to {output_dir / 'chunks.jsonl'}")


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
	"""Build the command-line argument parser and parse inputs."""

	parser = argparse.ArgumentParser(description="Create sentence-transformer embeddings for markdown corpus")
	parser.add_argument("--input", type=Path, default=INPUT_DIR, help="Root directory containing markdown files")
	parser.add_argument("--output", type=Path, default=OUTPUT_DIR, help="Directory to store embedding index")
	parser.add_argument("--model", default=MODEL, help="SentenceTransformer model name")
	parser.add_argument("--window-size", type=int, default=WINDOW_SIZE, help="Number of words per chunk")
	parser.add_argument("--stride", type=int, default=WINDOW_STRIDE, help="Word stride between windows")
	parser.add_argument("--batch-size", type=int, default=BATCH_SIZE, help="Batch size for embedding model")
	parser.add_argument("--no-normalize", action="store_true", help="Disable L2 normalisation of embeddings")
	return parser.parse_args(list(argv))


def main(argv: Iterable[str] | None = None) -> None:
	args = parse_args(argv or sys.argv[1:])

	normalize = not args.no_normalize

	build_index(
		input_dir=args.input,
		output_dir=args.output,
		window_size=args.window_size,
		stride=args.stride,
		model_name=args.model,
		batch_size=args.batch_size,
		normalize=normalize,
	)


if __name__ == "__main__":
	main()
