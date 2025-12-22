from mcq_generator import generate_mcqs_rag
items = generate_mcqs_rag("mathematics", 1)
print("generated items:", items)
print("generated_by:", [it.get("generated_by") for it in items])