import os
import io
import json
import csv
import time
from typing import List, Dict, Any

import streamlit as st

# import generator helpers from your project
from mcq_generator import load_blueprint, generate_mcqs_rag, generate_from_context

st.set_page_config(page_title="RAG MCQ Generator", layout="wide")

# load available subjects from blueprint; always include common defaults
try:
    blueprint = load_blueprint()
    structure = blueprint.get("structure", {}) or {}
    default_subjects = {"sat_english", "mathematics", "physics"}
    SUBJECTS = sorted(set(structure.keys()) | default_subjects) if structure is not None else sorted(default_subjects)
except Exception:
    SUBJECTS = ["sat_english","mathematics","physics"]

# --- UI: Sidebar controls ---------------------------------------------------
st.sidebar.title("Generation Controls")

# SUBJECTS already computed above

subject = st.sidebar.selectbox("Subject", options=SUBJECTS, index=0)
difficulty = st.sidebar.selectbox("Difficulty", options=["Easy", "Medium", "Hard"], index=1)
count = st.sidebar.number_input("Number of questions", min_value=1, max_value=20, value=5, step=1)

# Simple style tweaks (cute cards)
st.markdown(
    """
    <style>
    :root {
      --card-bg: #ffffff;
      --card-border: #d7dfeb;
      --card-shadow: 0 6px 16px rgba(17, 24, 39, 0.08);
      --text: #1b1f24;
      --muted: #566274;
      --chip-bg: #eaf2ff;
      --chip-text: #26323f;
      --choice-bg: #f7fafc;
      --choice-border: #e3e8ef;
      --correct: #2e7d32;
      --accent: #2563eb;
            --danger: #b91c1c;
    }
    .mcq-card {
                padding: 18px 20px; border-radius: 14px; margin-bottom: 18px;
        background: var(--card-bg);
        border: 1px solid var(--card-border);
        box-shadow: var(--card-shadow);
    }
    .card-header { margin-bottom: 10px; }
    .chip {
        display: inline-block; padding: 5px 12px; border-radius: 999px;
        background: var(--chip-bg); color: var(--chip-text); font-size: 12px; border: 1px solid #dbe7ff;
        margin-right: 6px; line-height: 1;
    }
    .chip-id { background: #eef3ff; }
    .chip-subject { background: #e3f2fd; }
    .chip-diff { background: #fff4e6; }
    .question { color: var(--text); font-size: 18px; line-height: 1.65; word-wrap: break-word; overflow-wrap: anywhere; }
    .q-label { font-weight: 700; color: var(--accent); margin-right: 4px; }
    .choice-row { margin: 8px 0; padding: 10px 12px; background: var(--choice-bg); border: 1px solid var(--choice-border); border-radius: 10px; color: var(--text); font-size: 16px; }
    .choice-key { display:inline-block; width: 24px; font-weight: 700; color: var(--text); }
    .ok { color: var(--correct); font-weight: 700; margin-left: 6px; }
    .meta { color: var(--muted); font-size: 12px; margin-top: 6px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Provider toggle: Auto / Gemini / Fallback
provider = st.sidebar.radio(
    "LLM Provider (force)",
    options=["Auto", "Gemini", "Fallback"],
    help="Auto = uses your configured LLM (Gemini). Fallback = local heuristic generator only."
)

st.sidebar.markdown("---")
st.sidebar.write("Quick actions")
if st.sidebar.button("Clear Streamlit Cache"):
    st.experimental_memo.clear()
    st.experimental_singleton.clear()
    st.sidebar.success("Cache cleared")

# --- helper: run generator with provider forcing ----------------------------
def _run_with_provider(provider_name: str, fn, *args, **kwargs):
    """Temporarily force provider by manipulating env keys inside this process."""
    snapshot = {
        "GEMINI_API_KEY": os.environ.get("GEMINI_API_KEY"),
    }
    try:
        if provider_name == "Gemini":
            # expect user has GEMINI_API_KEY set externally; if not, generation may fallback
            pass
        elif provider_name == "Fallback":
            os.environ["GEMINI_API_KEY"] = ""
        # Auto -> no changes
        return fn(*args, **kwargs)
    finally:
        # restore
        for k, v in snapshot.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v

# --- Main area --------------------------------------------------------------
st.title("RAG MCQ Generator — UI")
st.write("Generate grounded multiple-choice questions (MCQs) using RAG + LLM or a local fallback.")

col1, col2 = st.columns([3, 1])

with col2:
    st.markdown("### Controls")
    st.write(f"Provider: **{provider}**")
    st.write(f"Subject: **{subject}**")
    st.write(f"Difficulty: **{difficulty}**")
    st.write(f"Count: **{count}**")
    generate_btn = st.button("Generate MCQs")
    st.markdown("---")
    export_json_btn = st.button("Export last as JSON")
    export_csv_btn = st.button("Export last as CSV")

# container for results and messages
results_container = st.container()
status_text = st.empty()

# internal storage for last results
if "last_items" not in st.session_state:
    st.session_state["last_items"] = []

# run generation
if generate_btn:
    status_text.info("Generating MCQs — this may take a few seconds...")
    try:
        start = time.time()
        if provider == "Auto":
            items = _run_with_provider("Auto", generate_mcqs_rag, subject, int(count), difficulty)
        else:
            items = _run_with_provider(provider, generate_mcqs_rag, subject, int(count), difficulty)
    except Exception as e:
        status_text.error(f"Generation failed: {e}")
        items = []
    elapsed = time.time() - start
    status_text.success(f"Generation finished in {elapsed:.1f}s — {len(items)} items")
    st.session_state["last_items"] = items

# show results
items: List[Dict[str, Any]] = st.session_state.get("last_items", [])

if not items:
    results_container.info("No generated items yet. Click 'Generate MCQs' to start.")
else:
    for i, m in enumerate(items, start=1):
        q = m.get("question") or ""
        choices = m.get("choices", [])
        ans_idx = m.get("answer_idx", 0)
        gen_by = m.get("generated_by", "llm")
        citations = m.get("citations") or m.get("citation") or []
        if isinstance(citations, str):
            citations = [citations]

        card = st.container()
        # difficulty color hint
        diff = (difficulty or "").lower()
        diff_bg = {"easy":"#eaf7ea","medium":"#fff4e6","hard":"#fde7ef"}.get(diff, "#fff4e6")
        with card:
            st.markdown(
                f"<div class='mcq-card'>"
                f"<div class='card-header'><span class='chip chip-id'>#{i}</span>"
                f"<span class='chip chip-subject'>{subject}</span>"
                f"<span class='chip chip-diff' style='background:{diff_bg}'>"+difficulty+"</span></div>"
                f"<div class='question'><span class='q-label'>Q{i}.</span> {q}</div>"
                f"</div>",
                unsafe_allow_html=True,
            )
            for idx, c in enumerate(choices):
                mark = "<span class='ok'>✓</span>" if ans_idx == idx else ""
                st.markdown(f"<div class='choice-row'><span class='choice-key'>{chr(65+idx)}.</span> {c} {mark}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='meta'>Generated by: {gen_by} · Verified: {m.get('verified', False)}</div>", unsafe_allow_html=True)
            if citations:
                st.markdown("<div class='meta'>Citations:</div>", unsafe_allow_html=True)
                for c in citations:
                    st.markdown(f"<div class='meta'>• {c}</div>", unsafe_allow_html=True)
            rationale = m.get("rationale") or m.get("solution_latex") or ""
            if rationale:
                st.markdown("<div class='meta'>Rationale:</div>", unsafe_allow_html=True)
                if "$" in rationale or "\\" in rationale:
                    try:
                        st.latex(rationale)
                    except Exception:
                        st.text(rationale)
                else:
                    st.text(rationale)

# export buttons (write files to temp and provide downloads)
if export_json_btn and items:
    buf = io.StringIO()
    json.dump(items, buf, ensure_ascii=False, indent=2)
    b = buf.getvalue().encode("utf-8")
    st.download_button("Download JSON", data=b, file_name=f"{subject}_mcqs.json", mime="application/json")

if export_csv_btn and items:
    buf = io.StringIO()
    writer = csv.writer(buf)
    # header
    writer.writerow(["question", "choices", "answer", "verified", "generated_by", "citations", "rationale"])
    for it in items:
        writer.writerow([
            it.get("question",""),
            " | ".join(it.get("choices",[])),
            it.get("answer") or it.get("answer_idx"),
            str(it.get("verified", False)),
            it.get("generated_by",""),
            " | ".join(it.get("citations") or []),
            (it.get("rationale") or "").replace("\n"," "),
        ])
    b = buf.getvalue().encode("utf-8")
    st.download_button("Download CSV", data=b, file_name=f"{subject}_mcqs.csv", mime="text/csv")

st.markdown("---")
st.sidebar.markdown("App status & tips")
st.sidebar.write("Provider toggle forces which backend is used for generation.\n\nIf output looks noisy, try Fallback for heuristic questions or change Difficulty/Subject.")