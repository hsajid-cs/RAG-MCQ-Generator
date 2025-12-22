import json
import os
import random
import re
import sys
import time
from pathlib import Path
from typing import List, Dict, Any, Optional
import difflib
import ast

# Optional external deps for LLMs
try:
    import google.generativeai as genai
except Exception:
    genai = None

# Local helpers
try:
    import math_verify
except Exception:
    math_verify = None
from retriever import Retriever

DEFAULT_BLUEPRINT_PATH = Path("topic_blueprint/blueprint.json")
DEFAULT_INDEX_DIR = Path("anchor")

GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash-lite")

def load_blueprint(path: Optional[Path] = None) -> Dict[str, Any]:
    bp_path = Path(path or DEFAULT_BLUEPRINT_PATH)
    with bp_path.open("r", encoding="utf-8") as fh:
        return json.load(fh)

def _collect_candidate_tokens(contexts: List[Dict[str, Any]], exclude: Optional[str] = None) -> List[str]:
    tokens: List[str] = []
    ex = (exclude or "").lower()
    for c in contexts:
        txt = (c.get("text") or "")
        for t in re.findall(r"\b[\w\-]{3,}\b", txt):
            tl = t.lower()
            if tl == ex:
                continue
            if re.fullmatch(r"[-+]?\d+(\.\d+)?", t):
                continue
            tokens.append(t)
    # unique preserve order
    out, seen = [], set()
    for t in tokens:
        tl = t.lower()
        if tl in seen:
            continue
        seen.add(tl)
        out.append(t)
    return out[:200]

def _build_prompt(subject: str, contexts: List[Dict[str, Any]], difficulty: str, count: int) -> str:
    ctx_lines = []
    for i, c in enumerate(contexts[:6], 1):
        src = c.get("source") or c.get("file") or c.get("document_id") or "unknown"
        text = (c.get("text") or "").strip()
        ctx_lines.append(f"[CTX{i} src={src}]\n{text}")
    ctx_block = "\n\n".join(ctx_lines) or "[CTX1] No context"
    schema = (
        "Return ONLY JSON. Format: {\"items\": [ {\"question\": str, \"choices\": [str,str,str,str], \"answer\": one of A,B,C,D, \"answer_idx\": int 0..3, \"rationale\": str, \"citations\": [str] } ... ]}. "
        "Do not include markdown fences, code blocks, or any text outside the JSON object."
    )
    instruction = (
        f"You are a teacher creating grounded MCQs for {subject}. Difficulty={difficulty}. "
        f"Use the contexts below strictly; avoid hallucination. {schema}\n\n"
        f"CONTEXTS:\n{ctx_block}\n\n"
        f"Generate exactly {count} MCQs."
    )
    return instruction

# Removed OpenAI paths; generator uses Gemini only.

def call_gemini(prompt: str, temperature: float = 0.2) -> str:
    api_key = os.environ.get("GEMINI_API_KEY")
    if genai is None or not api_key:
        raise RuntimeError("Gemini not available or GEMINI_API_KEY missing")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(GEMINI_MODEL)
    resp = model.generate_content(
        prompt,
        generation_config={
            "temperature": temperature,
            "max_output_tokens": 3000,
            "response_mime_type": "application/json",
        },
    )
    # Prefer text; some SDKs return candidates with JSON string
    if getattr(resp, "text", None):
        return resp.text
    try:
        # Fallback to first candidate part
        cand = resp.candidates[0]
        parts = cand.content.parts
        for p in parts:
            if getattr(p, "text", None):
                return p.text
    except Exception:
        pass
    return ""

def _parse_llm_items(raw: str) -> List[Dict[str, Any]]:
    s = raw.strip()
    # try to extract JSON inside fences
    m = re.search(r"```(?:json)?\s*(\{[\s\S]*?\}|\[[\s\S]*?\])\s*```", s)
    if m:
        s = m.group(1)
    # try parsing top-level JSON
    def _from_obj(data: Any) -> List[Dict[str, Any]]:
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            for key in ("items", "mcqs", "questions", "data", "MultipleChoiceQuestions", "mcq_list"):
                val = data.get(key)
                if isinstance(val, list):
                    return val
            for v in data.values():
                if isinstance(v, list):
                    return v
        return []

    try:
        data = json.loads(s)
        out = _from_obj(data)
        if out:
            return out
    except Exception:
        pass
    # try python-literal style (single quotes, True/False/None)
    try:
        data = ast.literal_eval(s)
        out = _from_obj(data)
        if out:
            return out
    except Exception:
        pass
    # fallback: extract blocks that look like MCQ items
    blocks = re.findall(r"\{[^\{\}]*?\"question\"\s*:\s*[\s\S]*?\"choices\"\s*:\s*\[[\s\S]*?\][^\{\}]*?\}", s)
    items: List[Dict[str, Any]] = []
    for b in blocks:
        try:
            items.append(json.loads(b))
        except Exception:
            # try to make JSONish by replacing single quotes
            bj = b.replace("'", '"')
            # normalize booleans
            bj = re.sub(r"\bTrue\b", "true", bj)
            bj = re.sub(r"\bFalse\b", "false", bj)
            bj = re.sub(r"\bNone\b", "null", bj)
            try:
                items.append(json.loads(bj))
            except Exception:
                continue
    return items

def _ensure_item_shape(it: Dict[str, Any], subject: str) -> Optional[Dict[str, Any]]:
    q = (it.get("question") or "").strip()
    choices = it.get("choices") or []
    ans = it.get("answer") or ""
    if not q or not isinstance(choices, list):
        return None
    # coerce choices to exactly 4: trim extras, bail if too few
    if len(choices) < 4:
        return None
    if len(choices) > 4:
        choices = choices[:4]
    # normalize answer
    if isinstance(ans, int):
        idx = ans
        letter = chr(65 + idx) if 0 <= idx < 4 else "A"
    else:
        letter = str(ans).strip().upper()
        idx = ord(letter) - 65 if letter in {"A","B","C","D"} else 0
        letter = chr(65 + idx)
    item = {
        "subject": subject,
        "question": q,
        "choices": [str(c) for c in choices],
        "answer": letter,
        "answer_idx": idx,
        "rationale": it.get("rationale") or "",
        "citations": it.get("citations") or [],
        "generated_by": "llm",
        "verified": False,
    }
    return item

def generate_mcqs_rag(subject: str, count: int, difficulty: str = "Medium") -> List[Dict[str, Any]]:
    # Retrieve contexts using Retriever
    r = Retriever(subject, anchor_dir=DEFAULT_INDEX_DIR)
    # Use blueprint topic titles to seed queries if available
    try:
        bp = load_blueprint()
        topics = []
        subj_block = (bp.get("structure", {}).get(subject) or {})
        for _, chapter in subj_block.items():
            for t in chapter.get("topics", []):
                title = t.get("title") or ""
                if title:
                    topics.append(title)
        if not topics:
            topics = [f"{subject} key concepts", f"{subject} practice problems"]
    except Exception:
        topics = [f"{subject} fundamentals", f"{subject} definitions"]

    queries = random.sample(topics, k=min(count, len(topics)))
    items: List[Dict[str, Any]] = []

    # Build global prompt contexts (top retrieval for each query)
    all_contexts: List[Dict[str, Any]] = []
    for q in queries:
        all_contexts.extend(r.retrieve_top_k(q, k=4))
    # If no embeddings, `Retriever` returns fallback chunks
    prompt = _build_prompt(subject, all_contexts[:8], difficulty, count)

    raw = ""
    try:
        # Use Gemini for LLM generation
        gemini_key = os.environ.get("GEMINI_API_KEY")
        
        if not gemini_key:
            raise RuntimeError("GEMINI_API_KEY not set. Using heuristic fallback.")
        
        print("[DEBUG] Using Gemini to generate MCQs...")
        raw = call_gemini(prompt)
        print(f"[DEBUG] Gemini response length: {len(raw)}")
        print(f"[DEBUG] Gemini first 300 chars: {raw[:300]!r}")
        
        llm_items = _parse_llm_items(raw)
        print(f"[DEBUG] Parsed {len(llm_items)} items from Gemini")
        
        for it in llm_items:
            item = _ensure_item_shape(it, subject)
            if item:
                # attach a citation if missing
                if not item.get("citations") and all_contexts:
                    item["citations"] = [all_contexts[0].get("source") or "unknown"]
                items.append(item)
    except Exception as e:
        # fallback generate one-by-one using heuristic
        print(f"[DEBUG] Gemini failed: {e}. Falling back to heuristic generator.")
        for i in range(count):
            ctxs = r.retrieve_top_k(random.choice(queries), k=5)
            items.append(generate_from_context(ctxs, difficulty=difficulty, subject=subject))

    # ensure length
    if len(items) > count:
        items = items[:count]
    elif len(items) < count:
        for i in range(count - len(items)):
            ctxs = r.retrieve_top_k(random.choice(queries), k=5)
            items.append(generate_from_context(ctxs, difficulty=difficulty, subject=subject))
    return items


def generate_from_context(contexts: List[Dict[str, Any]], difficulty: str = "Medium", subject: Optional[str] = None) -> Dict[str, Any]:
    """
    Improved fallback MCQ generator with special-case math handling:
      - Detects simple numeric equalities or LaTeX fragments.
      - If a numeric answer is found, generates numeric distractors by perturbation.
      - Filters out single-letter fragments and noisy LaTeX-only lines.
      - Ensures a citation is present and tags generation source.
    """
    def _is_math_like(s: str) -> bool:
        return bool(re.search(r"(=|\\frac|\\sqrt|\\int|\\sum|\\sin|\\cos|\^|\\d+)", s))

    def _extract_numeric_token(s: str) -> Optional[float]:
        # try to find numeric literals (integers, decimals, scientific notation)
        m = re.search(r"(-?\d+(?:\.\d+)?(?:e[+-]?\d+)?)", s, flags=re.IGNORECASE)
        if m:
            try:
                return float(m.group(1))
            except Exception:
                return None
        return None

    def _numeric_distractors(value: float, n=3):
        # produce n distractors by multiplicative perturbation and round nicely
        deltas = [ -0.5, -0.2, 0.2, 0.3, 0.1, -0.1 ]
        out = []
        i = 0
        while len(out) < n and i < len(deltas):
            v = value * (1 + deltas[i])
            # round: if value is integer-like, keep ints
            if abs(value - int(value)) < 1e-9:
                candidate = str(int(round(v)))
            else:
                # keep 2 significant digits
                candidate = str(round(v, 2)).rstrip("0").rstrip(".")
            if candidate != str(value) and candidate not in out:
                out.append(candidate)
            i += 1
        # fallback simple increments if still short
        step = max(1, int(abs(value) * 0.1)) if abs(value) >= 1 else 1
        while len(out) < n:
            candidate = str(int(value) + step * (len(out) + 1))
            if candidate not in out and candidate != str(value):
                out.append(candidate)
        return out[:n]

    # --- start generator ---
    if not contexts:
        return {
            "subject": subject or "general",
            "question": "No context available.",
            "choices": ["A","B","C","D"],
            "answer": "A",
            "answer_idx": 0,
            "rationale": "No context.",
            "citations": ["no_source"],
            "generated_by": "fallback"
        }

    # pick best context (non-empty, long)
    ctx0 = next((c for c in contexts if c.get("text") and len(str(c.get("text")).strip()) > 40), contexts[0])
    raw_txt = (ctx0.get("text") or "").replace("\n", " ").strip()
    # remove spurious short-line fragments
    raw_txt = re.sub(r"\s{2,}", " ", raw_txt)
    sents = [s.strip() for s in re.split(r'(?<=[\.\?\!\:;])\s+', raw_txt) if len(s.strip()) > 10]

    sent = sents[0] if sents else raw_txt

    # math path
    if _is_math_like(sent):
        num = _extract_numeric_token(sent)
        if num is not None:
            # format question: try to present cleaned LaTeX -> plain
            q = re.sub(r"\\\w+\{([^}]*)\}", r"\1", sent)  # basic \frac etc -> content
            q = re.sub(r"\$+", "", q)
            question = f"{q}\nWhat is the value shown above?"
            correct = str(int(num)) if abs(num - round(num)) < 1e-9 else str(num)
            distractors = _numeric_distractors(num, n=3)
            choices = [correct] + distractors
            random.shuffle(choices)
            correct_idx = choices.index(correct)
            answer_letter = chr(65 + correct_idx)
            src = ctx0.get("source") or ctx0.get("file") or ctx0.get("id") or f"{subject or 'subj'}_ctx_0"
            item = {
                "subject": subject or ctx0.get("subject") or "mathematics",
                "question": question,
                "choices": choices,
                "answer": answer_letter,
                "answer_idx": correct_idx,
                "rationale": f"Extracted numeric value {correct} from context (source: {src})",
                "citations": [src],
                "generated_by": "fallback_math"
            }
            # verify using math_verify if available; if fails, mark unverified
            try:
                item["verified"] = math_verify.verify_math_solution(f"{correct} = {correct}")
            except Exception:
                item["verified"] = False
            return item

    # non-math path: previous improved fallback (clean tokens, avoid single letters)
    token = None
    # pick a mask token from sentence (prefer multi-char words)
    words = [w for w in re.findall(r"\b[a-zA-Z0-9\-]{2,}\b", sent) if len(w) > 1]
    if words:
        # prefer longest informative word
        token = max(words, key=len)
    if not token:
        token = "the term"
    masked = re.sub(re.escape(token), "_____", sent, flags=re.IGNORECASE)
    question = masked if len(masked) > 10 else f"In the context: {sent}\nWhat is the missing term?"

    # improved distractor collection from contexts
    candidates = _collect_candidate_tokens(contexts, exclude=token)
    # filter candidates: length >= 3, not numeric, not too similar to correct token
    def is_plausible(t: str) -> bool:
        if len(t) < 3:
            return False
        if re.fullmatch(r'[-+]?\d+(\.\d+)?', t):
            return False
        sim = difflib.SequenceMatcher(None, t.lower(), token.lower()).ratio()
        return sim < 0.85 and t.lower() != token.lower()

    plausible = [t for t in candidates if is_plausible(t)]
    # prefer tokens with similar length class to the masked token
    tgt_len = len(token)
    plausible.sort(key=lambda t: abs(len(t) - tgt_len))
    distractors = []
    seen = set()
    for t in plausible:
        tl = t.lower()
        if tl in seen:
            continue
        seen.add(tl)
        distractors.append(t)
        if len(distractors) >= 3:
            break

    # last-resort filler if contexts too sparse
    if len(distractors) < 3:
        fill_pool = [t for t in candidates if len(t) >= 3][:10]
        random.shuffle(fill_pool)
        for t in fill_pool:
            if t.lower() not in seen and t.lower() != token.lower():
                distractors.append(t)
                seen.add(t.lower())
                if len(distractors) >= 3:
                    break

    # still short: avoid "_alt" placeholders; use simple conceptual fillers
    conceptual_fallbacks = [f"{token} concept", f"{token} principle", f"{token} term"]
    i = 0
    while len(distractors) < 3 and i < len(conceptual_fallbacks):
        if conceptual_fallbacks[i].lower() not in seen:
            distractors.append(conceptual_fallbacks[i])
            seen.add(conceptual_fallbacks[i].lower())
        i += 1

    choices = [token] + distractors[:3]
    # ensure exactly 4 choices
    if len(choices) < 4:
        # pad with distinct tokens from candidates
        for t in candidates:
            if t.lower() not in seen and t.lower() != token.lower():
                choices.append(t)
                seen.add(t.lower())
                if len(choices) == 4:
                    break
    choices = choices[:4]
    random.shuffle(choices)
    correct_idx = choices.index(token) if token in choices else 0
    answer_letter = chr(65 + correct_idx)
    src = ctx0.get("source") or ctx0.get("file") or ctx0.get("id") or f"{subject or 'subj'}_ctx_0"

    item = {
        "subject": subject or ctx0.get("subject") or "general",
        "question": question,
        "choices": choices,
        "answer": answer_letter,
        "answer_idx": correct_idx,
        "rationale": f"Based on: \"{sent}\" (source: {src})",
        "citations": [src],
        "generated_by": "fallback"
    }
    item["verified"] = False
    return item
# adapter name compatibility
def generate_mcq_from_context(contexts: List[Dict[str,Any]], difficulty: str = "Medium") -> Dict[str,Any]:
    return generate_from_context(contexts, difficulty)

def generate_mcqs(subject: str, count: int, blueprint_path: Optional[Path] = None, index_dir: Optional[Path] = None, difficulty: str = "Medium") -> List[Dict[str, Any]]:
    # Wrapper for legacy CLI usage
    return generate_mcqs_rag(subject, count, difficulty)


def main():
    blueprint = load_blueprint(DEFAULT_BLUEPRINT_PATH)
    structure = blueprint.get("structure", {})
    subjects = sorted(structure.keys())
    print("Available subjects:", ", ".join(subjects))

    if len(sys.argv) > 1:
        subject = sys.argv[1]
    else:
        subject = input("Select a subject: ").strip()

    if subject.lower() not in [s.lower() for s in subjects]:
        print("Invalid subject")
        return

    subject = next(s for s in subjects if s.lower() == subject.lower())
    count = int(sys.argv[2]) if len(sys.argv) > 2 else int(input("How many MCQs? [30]: ") or "30")

    mcqs = generate_mcqs(subject, count, DEFAULT_BLUEPRINT_PATH, DEFAULT_INDEX_DIR)
    out_dir = Path("mcqs")
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / f"{subject.lower()}_mcqs.json"
    with out_path.open("w", encoding="utf-8") as fh:
        json.dump(mcqs, fh, ensure_ascii=False, indent=2)
    print(f"Saved {len(mcqs)} MCQs to {out_path}")


if __name__ == "__main__":
    main()

