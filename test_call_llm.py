from mcq_generator import call_llm
prompt = "Write one short JSON 4-choice MCQ about photosynthesis with keys: subject, question, choices, answer, rationale, citation"
print("Calling LLM...")
resp = call_llm(prompt)
print("LLM responded (len):", len(resp or ""))
print("---- START RAW ----")
print((resp or "")[:4000])
print("---- END RAW ----")