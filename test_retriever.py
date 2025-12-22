#!/usr/bin/env python3
"""Test retriever to verify RAG index is working."""
from retriever import Retriever
from pathlib import Path

# Test math retriever
print("[TEST] Loading Retriever for 'mathematics'...")
try:
    r = Retriever("mathematics", anchor_dir=Path("anchor"))
    print(f"✓ Retriever loaded. Chunks: {len(r.chunks)}, Embeddings shape: {r.emb.shape}")
except Exception as e:
    print(f"✗ Error loading retriever: {e}")
    exit(1)

# Test retrieval
print("\n[TEST] Retrieving top-5 for 'quadratic equations'...")
try:
    results = r.retrieve_top_k("quadratic equations", k=5)
    print(f"✓ Retrieved {len(results)} chunks")
    for i, chunk in enumerate(results, 1):
        src = chunk.get("source") or chunk.get("document_id") or "unknown"
        score = chunk.get("score", 0)
        text = (chunk.get("text") or "")[:100]
        print(f"  [{i}] {src} (score={score:.3f})\n      {text}...")
except Exception as e:
    print(f"✗ Error retrieving: {e}")
    import traceback
    traceback.print_exc()
    exit(1)

print("\n✓ Retriever is working!")
