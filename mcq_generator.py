import json
import random
import re
import sys
import time
from pathlib import Path
from typing import Any, Dict, List

import numpy as np
import google.generativeai as genai
from sentence_transformers import SentenceTransformer
# Configuration
GEMINI_API_KEY = "AIzaSyAXXDD1M89vEiDL9uP5ke-viAOz7hmb8ck"
MODEL_NAME = "gemini-2.5-flash-lite"

# Configure genai
genai.configure(api_key=GEMINI_API_KEY)
DEFAULT_INDEX_DIR = Path("anchor")
DEFAULT_BLUEPRINT_PATH = Path("topic_blueprint") / "blueprint.json"
DEFAULT_EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
DEFAULT_TOP_K = 5

# Rate limiting to prevent API overload
BATCH_SIZE = 5  # Generate 5 questions per API call
DELAY_BETWEEN_BATCHES = 2  # Seconds to wait between batches


def clean_latex(text: str) -> str:
	"""Remove or simplify LaTeX markup."""
	text = re.sub(r'\$\$.*?\$\$', '[Math]', text, flags=re.DOTALL)
	text = re.sub(r'\$([^\$]+)\$', r'\1', text)
	text = re.sub(r'\\[a-zA-Z]+\{([^\}]*)\}', r'\1', text)
	text = re.sub(r'\\[a-zA-Z]+', '', text)
	text = re.sub(r'\s+', ' ', text)
	return text.strip()


def load_embeddings(index_dir: Path) -> tuple[np.ndarray, List[Dict[str, Any]], SentenceTransformer]:
	"""Load embeddings, chunks, and encoder."""
	embeddings_path = index_dir / "embeddings.npy"
	chunks_path = index_dir / "chunks.jsonl"
	
	embeddings = np.load(embeddings_path)
	chunks = []
	with chunks_path.open("r", encoding="utf-8") as f:
		for line in f:
			chunks.append(json.loads(line))
	
	encoder = SentenceTransformer(DEFAULT_EMBEDDING_MODEL)
	return embeddings, chunks, encoder


def retrieve_context(query: str, embeddings: np.ndarray, chunks: List[Dict], encoder: SentenceTransformer, top_k: int = 5) -> str:
	"""Retrieve top-k relevant chunks for a query."""
	query_embedding = encoder.encode([query], normalize_embeddings=True)[0]
	similarities = np.dot(embeddings, query_embedding)
	top_indices = np.argsort(similarities)[::-1][:top_k]
	
	results = []
	for idx in top_indices:
		chunk_text = chunks[idx].get("text", "")
		results.append(clean_latex(chunk_text))
	
	return " ".join(results)


def call_gemini(prompt: str, temperature: float = 0.2, max_tokens: int = 8192) -> str:
	"""Call Gemini API using google.generativeai library."""
	model = genai.GenerativeModel(MODEL_NAME)
	
	generation_config = genai.types.GenerationConfig(
		temperature=temperature,
		max_output_tokens=max_tokens,
	)
	
	response = model.generate_content(
		prompt,
		generation_config=generation_config,
	)
	
	return response.text.strip()


def build_batch_prompt(topics: List[Dict[str, Any]], contexts: List[str]) -> str:
	"""Build prompt for batch MCQ generation."""
	items_text = []
	for idx, (topic, context) in enumerate(zip(topics, contexts), 1):
		items_text.append(f"""
### Topic {idx}
Subject: {topic['subject']}
Grade: {topic['grade']}
Chapter: {topic['chapter']}
Topic: {topic['topic']}
Citation: {topic['citation']}
Context:
{context.strip()}
""")
	
	header = f"""Generate exactly {len(topics)} multiple choice questions as a JSON array.

IMPORTANT: Output ONLY valid JSON. No markdown, no code fences, no commentary.
Clean all LaTeX from questions and choices - use plain text only.

Each object must have these exact keys:
- subject (string)
- grade (string)  
- chapter (string)
- topic (string)
- question (string, clean text, no LaTeX)
- choices (array of exactly 4 strings labeled A-D, clean text, no LaTeX)
- answer (string, one of "A", "B", "C", "D")
- rationale (string, explain why answer is correct)
- citation (string, use the provided citation path)

Topics:"""
	
	return header + "\n" + "\n".join(items_text)


def parse_json_response(raw: str) -> List[Dict[str, Any]]:
	"""Parse JSON from Gemini response, stripping markdown fences."""
	text = raw.strip()
	
	# Remove markdown code fences
	if text.startswith("```"):
		lines = text.splitlines()
		if lines:
			lines = lines[1:]  # Remove first line (```json or ```)
		if lines and lines[-1].strip().startswith("```"):
			lines = lines[:-1]  # Remove last line (```)
		text = "\n".join(lines).strip()
	
	# Try direct parse
	try:
		data = json.loads(text)
		if isinstance(data, list):
			return data
	except json.JSONDecodeError:
		pass
	
	# Try finding JSON array brackets
	start = text.find("[")
	end = text.rfind("]")
	if start != -1 and end != -1:
		fragment = text[start:end + 1]
		try:
			data = json.loads(fragment)
			if isinstance(data, list):
				return data
		except json.JSONDecodeError:
			pass
	
	raise ValueError(f"Could not parse JSON from response")


def load_blueprint(blueprint_path: Path) -> Dict[str, Any]:
	"""Load blueprint file."""
	with blueprint_path.open("r", encoding="utf-8") as f:
		return json.load(f)


def get_topics_for_subject(blueprint: Dict[str, Any], subject: str) -> List[Dict[str, Any]]:
	"""Extract topics for a subject from blueprint."""
	topics = []
	structure = blueprint.get("structure", {})
	
	for subj_key, subj_data in structure.items():
		if subj_key.lower() != subject.lower():
			continue
		
		for grade_key, chapters in subj_data.items():
			grade = grade_key.replace("Grade ", "")
			
			for chap_key, chap_info in chapters.items():
				chap_num = chap_key.replace("Chapter ", "")
				chap_title = chap_info.get("title", "")
				
				for topic in chap_info.get("topics", []):
					topic_file = topic.get("file")
					if not topic_file:
						continue
					
					topics.append({
						"subject": subj_key,
						"grade": grade,
						"chapter": f"{chap_num}: {chap_title}",
						"topic": topic.get("title", ""),
						"citation": topic_file,
					})
	
	return topics


def generate_mcqs(subject: str, count: int, blueprint_path: Path, index_dir: Path) -> List[Dict[str, Any]]:
	"""Generate MCQs using RAG and Gemini."""
	print("Loading embeddings...")
	embeddings, chunks, encoder = load_embeddings(index_dir)
	print(f"Loaded {len(chunks)} chunks\n")
	
	print("Loading blueprint...")
	blueprint = load_blueprint(blueprint_path)
	
	topics = get_topics_for_subject(blueprint, subject)
	if not topics:
		raise ValueError(f"No topics found for subject '{subject}'")
	
	print(f"Found {len(topics)} topics for {subject}")
	
	# Randomly select topics
	random.shuffle(topics)
	selected = topics[:count]
	
	print(f"\nGenerating {count} MCQs in batches of {BATCH_SIZE}...")
	print(f"Rate limiting: {DELAY_BETWEEN_BATCHES}s delay between batches\n")
	
	all_mcqs = []
	
	# Process in batches
	for batch_start in range(0, len(selected), BATCH_SIZE):
		batch_end = min(batch_start + BATCH_SIZE, len(selected))
		batch = selected[batch_start:batch_end]
		
		print(f"Batch {batch_start // BATCH_SIZE + 1}: Processing questions {batch_start + 1}-{batch_end}...")
		
		# Retrieve context for each topic in batch
		contexts = []
		for topic in batch:
			query = f"{topic['subject']} {topic['topic']} {topic['chapter']}"
			context = retrieve_context(query, embeddings, chunks, encoder, top_k=DEFAULT_TOP_K)
			contexts.append(context)
		
		# Build prompt and call Gemini
		prompt = build_batch_prompt(batch, contexts)
		
		try:
			raw_response = call_gemini(prompt)
			batch_mcqs = parse_json_response(raw_response)
			
			# Validate and add to results
			if len(batch_mcqs) == len(batch):
				all_mcqs.extend(batch_mcqs)
				print(f"  ✓ Generated {len(batch_mcqs)} MCQs")
			else:
				print(f"  ⚠ Expected {len(batch)} MCQs but got {len(batch_mcqs)}")
				all_mcqs.extend(batch_mcqs)
			
			# Rate limiting: wait between batches to avoid API overload
			if batch_end < len(selected):
				print(f"  ⏳ Waiting {DELAY_BETWEEN_BATCHES}s before next batch...")
				time.sleep(DELAY_BETWEEN_BATCHES)
		
		except Exception as e:
			print(f"  ✗ Error in batch: {e}")
			# Wait longer on error before retrying
			if batch_end < len(selected):
				print(f"  ⏳ Waiting {DELAY_BETWEEN_BATCHES * 2}s after error...")
				time.sleep(DELAY_BETWEEN_BATCHES * 2)
			continue
	
	print(f"\n✓ Successfully generated {len(all_mcqs)} MCQs")
	return all_mcqs


def main():
	"""Main entry point."""
	# Load blueprint to get available subjects
	blueprint = load_blueprint(DEFAULT_BLUEPRINT_PATH)
	structure = blueprint.get("structure", {})
	subjects = sorted(structure.keys())
	
	print("Available subjects:")
	for subj in subjects:
		print(f"  - {subj}")
	
	# Get subject from command line or prompt
	if len(sys.argv) > 1:
		subject = sys.argv[1]
		print(f"\nUsing subject from command line: {subject}")
	else:
		subject = input("\nSelect a subject: ").strip()
	
	if subject.lower() not in [s.lower() for s in subjects]:
		print("Invalid subject")
		return
	
	# Match case-insensitive
	subject = next(s for s in subjects if s.lower() == subject.lower())
	
	# Get count from command line or prompt
	if len(sys.argv) > 2:
		count = int(sys.argv[2])
		print(f"Generating {count} MCQs (from command line argument)")
	else:
		count_input = input("How many MCQs? [30]: ").strip()
		count = int(count_input) if count_input else 30
	
	# Generate MCQs
	mcqs = generate_mcqs(subject, count, DEFAULT_BLUEPRINT_PATH, DEFAULT_INDEX_DIR)
	
	# Save output
	output_dir = Path("mcqs")
	output_dir.mkdir(exist_ok=True)
	output_path = output_dir / f"{subject.lower()}_mcqs.json"
	
	with output_path.open("w", encoding="utf-8") as f:
		json.dump(mcqs, f, ensure_ascii=False, indent=2)
	
	print(f"\n✓ Saved {len(mcqs)} MCQs to {output_path}")


if __name__ == "__main__":
	main()
