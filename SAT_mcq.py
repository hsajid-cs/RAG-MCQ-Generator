"""SAT English Grammar & Writing MCQ Generator using RAG and Gemini API.

This script generates SAT-style multiple choice questions for grammar and writing
concepts based on the cleaned SAT English corpus.
"""

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
GEMINI_API_KEY = "AIzaSyCXmLZgi3fIBplor9rTue9f93t0EmmWeCI"
MODEL_NAME = "gemini-2.5-flash-lite"

# Configure genai
genai.configure(api_key=GEMINI_API_KEY)

ANCHOR_DIR = Path("anchor")
BLUEPRINT_PATH = Path("blueprint") / "blueprint_sat_english.json"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
TOP_K = 5
EMBEDDINGS_FILE = "sat_english_embeddings.npy"
CHUNKS_FILE = "sat_english_chunks.jsonl"

# Rate limiting to prevent API overload
BATCH_SIZE = 5  # Generate 5 questions per API call
DELAY_BETWEEN_BATCHES = 2  # Seconds to wait between batches


def load_sat_embeddings(anchor_dir: Path) -> tuple[np.ndarray, List[Dict[str, Any]], SentenceTransformer]:
    """Load SAT English embeddings, chunks, and encoder."""
    embeddings_path = anchor_dir / EMBEDDINGS_FILE
    chunks_path = anchor_dir / CHUNKS_FILE
    
    print(f"Loading embeddings from {embeddings_path}...")
    embeddings = np.load(embeddings_path)
    
    print(f"Loading chunks from {chunks_path}...")
    chunks = []
    with chunks_path.open("r", encoding="utf-8") as f:
        for line in f:
            chunks.append(json.loads(line))
    
    print(f"Loading encoder: {EMBEDDING_MODEL}...")
    encoder = SentenceTransformer(EMBEDDING_MODEL)
    
    return embeddings, chunks, encoder


def retrieve_context(
    query: str,
    embeddings: np.ndarray,
    chunks: List[Dict],
    encoder: SentenceTransformer,
    top_k: int = 5
) -> tuple[str, List[str]]:
    """Retrieve top-k relevant chunks for a query.
    
    Returns:
        Combined context text and list of source citations
    """
    query_embedding = encoder.encode([query], normalize_embeddings=True)[0]
    similarities = np.dot(embeddings, query_embedding)
    top_indices = np.argsort(similarities)[::-1][:top_k]
    
    results = []
    citations = []
    
    for idx in top_indices:
        chunk = chunks[idx]
        chunk_text = chunk.get("text", "")
        results.append(chunk_text)
        
        # Build citation from metadata
        doc_id = chunk.get("document_id", "")
        citations.append(doc_id)
    
    # Deduplicate citations
    citations = list(dict.fromkeys(citations))
    
    return " ".join(results), citations


def call_gemini(prompt: str, temperature: float = 0.3, max_tokens: int = 8192) -> str:
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


def build_sat_mcq_prompt(topics: List[Dict[str, Any]], contexts: List[tuple[str, List[str]]]) -> str:
    """Build prompt for SAT-style MCQ generation."""
    
    items_text = []
    for idx, (topic, (context, citations)) in enumerate(zip(topics, contexts), 1):
        items_text.append(f"""
### Question {idx}
Chapter: {topic['chapter']}
Topic: {topic['topic']}
Citations: {', '.join(citations[:2])}

Context (Educational Content):
{context[:1500]}
""")
    
    header = f"""You are an expert SAT Writing and Language test creator. Generate exactly {len(topics)} multiple choice questions in the EXACT style of the SAT Writing and Language Test.

CRITICAL REQUIREMENTS:

1. Output ONLY valid JSON array. No markdown, no code fences, no commentary.

2. QUESTION STRUCTURE - Each question MUST follow this exact format:
   - Start with a passage (2-4 sentences of context)
   - Mark ONE portion with **underlined text** (use **text** format)
   - End with: "Which choice best replaces the underlined portion?" OR similar question
   - The underlined portion should contain the error or improvement point

3. AUTHENTIC SAT FORMAT EXAMPLES:

   Example 1 (Grammar):
   "The research team **has discovered** several new species of insects in the rainforest. Their findings will be published next month."
   Question: "Which choice best replaces the underlined portion?"
   A) NO CHANGE
   B) have discovered
   C) are discovering  
   D) discovered

   Example 2 (Punctuation):
   "Marie Curie was a pioneering scientist**,** she won two Nobel Prizes in different fields."
   Question: "Which choice best corrects the underlined portion?"
   A) NO CHANGE
   B) scientist;
   C) scientist. She
   D) scientist, and she

   Example 3 (Rhetoric):
   "Solar panels convert sunlight into electricity. **This process helps reduce carbon emissions.** Wind turbines are another renewable energy source."
   Question: "The writer is considering deleting the underlined sentence. Should it be kept or deleted?"
   A) Kept, because it explains the environmental benefit.
   B) Kept, because it contrasts with wind energy.
   C) Deleted, because it interrupts the flow.
   D) Deleted, because it doesn't relate to solar panels.

4. EACH MCQ JSON OBJECT MUST HAVE:
   - "chapter": string (chapter name from context)
   - "topic": string (topic from context)
   - "concept": string (SPECIFIC concept: "comma splice", "subject-verb agreement", "parallelism", "transition logic", etc.)
   - "passage": string (2-4 sentences with **underlined portion**)
   - "question": string (The actual question being asked)
   - "choices": array of EXACTLY 4 strings (A, B, C, D format - include "A) " prefix)
   - "answer": string (one of "A", "B", "C", "D")
   - "rationale": string (explain why answer is correct AND why others are wrong)
   - "citations": array of strings (source paths)
   - "difficulty": string ("easy", "medium", or "hard")

5. CHOICES FORMAT:
   - ALWAYS include "A) NO CHANGE" when testing errors
   - Each choice must start with letter and parenthesis: "A) ", "B) ", "C) ", "D) "
   - Choices should be CONCISE - just the replacement text
   - Make distractors realistic (common student errors)

6. CONCEPT VARIETY - Test these across all questions:
   - Punctuation: comma splices, semicolons, colons, apostrophes
   - Grammar: subject-verb agreement, pronoun agreement, verb tense
   - Sentence Structure: fragments, run-ons, sentence combining
   - Rhetoric: add/delete/revise, word choice, transitions
   - Style: conciseness, parallelism, modifier placement

7. QUALITY RULES:
   - Passage MUST be clear and readable
   - Underlined portion MUST be clearly marked with **asterisks**
   - Question MUST be specific and unambiguous
   - ONE correct answer, three plausible distractors
   - Rationale MUST explain the grammar rule

Topics:"""
    
    return header + "\n" + "\n".join(items_text) + "\n\nGenerate JSON array:"


def parse_json_response(raw: str) -> List[Dict[str, Any]]:
    """Parse JSON from Gemini response, handling markdown fences."""
    text = raw.strip()
    
    # Remove markdown code fences
    if text.startswith("```"):
        lines = text.splitlines()
        if lines:
            # Remove first line (```json or ```)
            lines = lines[1:]
        if lines and lines[-1].strip().startswith("```"):
            # Remove last line (```)
            lines = lines[:-1]
        text = "\n".join(lines).strip()
    
    # Try direct parse
    try:
        data = json.loads(text)
        if isinstance(data, list):
            return data
        elif isinstance(data, dict) and "questions" in data:
            return data["questions"]
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
    
    raise ValueError(f"Could not parse JSON from response. Response preview: {text[:500]}")


def load_blueprint(blueprint_path: Path) -> Dict[str, Any]:
    """Load SAT English blueprint file."""
    if not blueprint_path.exists():
        raise FileNotFoundError(f"Blueprint not found: {blueprint_path}")
    
    with blueprint_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def get_sat_topics(blueprint: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Extract all topics from SAT English blueprint."""
    topics = []
    structure = blueprint.get("structure", {})
    
    sat_data = structure.get("sat_english", {})
    
    for chapter_key, chapter_info in sat_data.items():
        chapter_title = chapter_info.get("title", chapter_key)
        
        for topic in chapter_info.get("topics", []):
            topic_file = topic.get("file")
            topic_title = topic.get("title", "")
            
            if not topic_file or not topic_title:
                continue
            
            topics.append({
                "chapter": chapter_title,
                "topic": topic_title,
                "citation": topic_file,
            })
    
    return topics


def generate_sat_mcqs(
    count: int,
    blueprint_path: Path,
    anchor_dir: Path,
    output_path: Path | None = None
) -> List[Dict[str, Any]]:
    """Generate SAT English MCQs using RAG and Gemini.
    
    Args:
        count: Number of MCQs to generate
        blueprint_path: Path to blueprint JSON file
        anchor_dir: Directory containing embeddings and chunks
        output_path: Optional output file path
    
    Returns:
        List of generated MCQ dictionaries
    """
    print("\n" + "="*70)
    print("SAT English MCQ Generator")
    print("="*70 + "\n")
    
    # Load resources
    embeddings, chunks, encoder = load_sat_embeddings(anchor_dir)
    print(f"✓ Loaded {len(chunks)} chunks\n")
    
    blueprint = load_blueprint(blueprint_path)
    print(f"✓ Loaded blueprint from {blueprint_path}\n")
    
    topics = get_sat_topics(blueprint)
    if not topics:
        raise ValueError("No topics found in blueprint")
    
    print(f"✓ Found {len(topics)} topics\n")
    
    # Randomly select topics
    random.shuffle(topics)
    selected = topics[:count]
    
    print(f"Generating {count} MCQs in batches of {BATCH_SIZE}...\n")
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
            query = f"{topic['chapter']} {topic['topic']}"
            context, citations = retrieve_context(query, embeddings, chunks, encoder, top_k=TOP_K)
            contexts.append((context, citations))
        
        # Build prompt and call Gemini
        prompt = build_sat_mcq_prompt(batch, contexts)
        
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
    
    print(f"\n{'='*70}")
    print(f"✅ Successfully generated {len(all_mcqs)} SAT English MCQs")
    print(f"{'='*70}\n")
    
    # Save output if path provided
    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", encoding="utf-8") as f:
            json.dump(all_mcqs, f, ensure_ascii=False, indent=2)
        print(f"✓ Saved MCQs to {output_path}\n")
    
    return all_mcqs


def print_sample_mcq(mcq: Dict[str, Any]) -> None:
    """Pretty print a single MCQ."""
    print("\n" + "="*70)
    print(f"Chapter: {mcq.get('chapter', 'N/A')}")
    print(f"Topic: {mcq.get('topic', 'N/A')}")
    print(f"Concept: {mcq.get('concept', 'N/A')}")
    print(f"Difficulty: {mcq.get('difficulty', 'N/A')}")
    print("-"*70)
    
    # Print passage if available
    passage = mcq.get('passage', '')
    if passage:
        print(f"\nPASSAGE:\n{passage}\n")
    
    # Print question
    question = mcq.get('question', '')
    print(f"QUESTION:\n{question}\n")
    
    # Print choices
    choices = mcq.get('choices', [])
    for choice in choices:
        label = choice[0] if choice and choice[0] in 'ABCD' else '?'
        marker = "✓" if label == mcq.get('answer') else " "
        print(f"{marker} {choice}")
    
    print(f"\nCORRECT ANSWER: {mcq.get('answer', 'N/A')}")
    print(f"\nRATIONALE:\n{mcq.get('rationale', 'N/A')}")
    print("="*70)


def main():
    """Main entry point."""
    print("\n" + "="*70)
    print("SAT English MCQ Generator")
    print("="*70)
    
    # Get user input (from command line argument or prompt)
    if len(sys.argv) > 1:
        count = int(sys.argv[1])
        print(f"\nGenerating {count} MCQs (from command line argument)")
    else:
        count_input = input("\nHow many MCQs would you like to generate? [10]: ").strip()
        count = int(count_input) if count_input else 10
    
    print(f"\n📊 Configuration:")
    print(f"  - Questions to generate: {count}")
    print(f"  - Batch size: {BATCH_SIZE} questions per API call")
    print(f"  - Delay between batches: {DELAY_BETWEEN_BATCHES}s")
    print(f"  - Estimated time: ~{(count // BATCH_SIZE + 1) * DELAY_BETWEEN_BATCHES} seconds\n")
    
    # Generate MCQs
    output_dir = Path("mcqs")
    output_path = output_dir / "sat_english_mcqs.json"
    
    mcqs = generate_sat_mcqs(
        count=count,
        blueprint_path=BLUEPRINT_PATH,
        anchor_dir=ANCHOR_DIR,
        output_path=output_path
    )


if __name__ == "__main__":
    main()
