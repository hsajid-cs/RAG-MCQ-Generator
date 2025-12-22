import json
from pathlib import Path
from typing import List, Dict, Any, Optional

import numpy as np

try:
    from embed import embed_texts  # expected: List[str] -> np.ndarray (n, d)
except Exception:
    embed_texts = None


def _cosine_similarity_vec(query_vec: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    """Return cosine similarities between query_vec (d,) and matrix (n,d)."""
    if matrix.size == 0:
        return np.array([])
    qn = np.linalg.norm(query_vec)
    mn = np.linalg.norm(matrix, axis=1)
    # avoid division by zero
    if qn == 0:
        qn = 1e-12
    mn[mn == 0] = 1e-12
    sims = (matrix @ query_vec) / (mn * qn)
    return sims


class Retriever:
    """
    File-backed retriever that uses precomputed embeddings (numpy) and chunk JSONL.

    Usage:
      r = Retriever("sat_english")
      topk = r.retrieve_top_k("identify the grammar error", k=6)
    """

    def __init__(self, subject: str, anchor_dir: Optional[Path] = None):
        self.subject = subject.lower().replace(" ", "_")
        self.anchor_dir = Path(anchor_dir or "anchor")
        # candidate filenames
        emb_path = self.anchor_dir / f"{self.subject}_embeddings.npy"
        chunks_path = self.anchor_dir / f"{self.subject}_chunks.jsonl"

        # fallback to generic index folder names
        if not emb_path.exists() or not chunks_path.exists():
            emb_path = self.anchor_dir / "embeddings.npy"
            chunks_path = self.anchor_dir / "chunks.jsonl"

        if not emb_path.exists():
            raise FileNotFoundError(f"Embeddings file not found: {emb_path}")
        if not chunks_path.exists():
            raise FileNotFoundError(f"Chunks file not found: {chunks_path}")

        self.emb = np.load(str(emb_path))
        # ensure 2D
        if self.emb.ndim == 1:
            self.emb = self.emb.reshape(1, -1)

        # load chunks (jsonl)
        self.chunks: List[Dict[str, Any]] = []
        with open(chunks_path, "r", encoding="utf-8") as fh:
            for line in fh:
                try:
                    self.chunks.append(json.loads(line))
                except Exception:
                    continue

        if len(self.chunks) != self.emb.shape[0]:
            # proceed but warn
            print(
                f"[retriever] warning: #chunks ({len(self.chunks)}) != #embeddings ({self.emb.shape[0]})"
            )

    def retrieve_top_k(self, query: str, k: int = 5, use_embed_fn: Optional[callable] = None) -> List[Dict[str, Any]]:
        """
        Return top-k chunks for `query`. Each returned dict includes fields:
          - original chunk fields (must include 'text' or similar)
          - score: float cosine similarity
          - source: provenance id/path if present in chunk
        """
        # choose embedding function
        embed_fn = use_embed_fn or embed_texts
        if embed_fn is None:
            # fallback: return first k chunks with score 1.0
            return [
                {**(self.chunks[i] if i < len(self.chunks) else {}), "score": 1.0, "source": (self.chunks[i].get("source") if i < len(self.chunks) else "unknown")}
                for i in range(min(k, len(self.chunks)))
            ]

        qvecs = embed_fn([query])
        if isinstance(qvecs, list):
            qvec = np.array(qvecs[0], dtype=float)
        else:
            qvec = np.array(qvecs[0], dtype=float)

        sims = _cosine_similarity_vec(qvec, self.emb)
        if sims.size == 0:
            return []
        idx = np.argsort(sims)[::-1][:k]
        results: List[Dict[str, Any]] = []
        for i in idx:
            chunk = self.chunks[i].copy() if i < len(self.chunks) else {}
            chunk["score"] = float(sims[i])
            # normalize provenance keys (prefer document_id written by embed.py)
            chunk["source"] = (
                chunk.get("source")
                or chunk.get("file")
                or chunk.get("document_id")
                or chunk.get("id")
                or "unknown"
            )
            results.append(chunk)
        return results


if __name__ == "__main__":
    # quick local smoke test (requires embed.embed_texts + anchor files)
    import sys

    subj = sys.argv[1] if len(sys.argv) > 1 else "sat_english"
    query = sys.argv[2] if len(sys.argv) > 2 else "example question"
    r = Retriever(subj)
    top = r.retrieve_top_k(query, k=5)
    for i, t in enumerate(top, 1):
        print(i, t.get("source"), t.get("score"), (t.get("text") or "")[:120])