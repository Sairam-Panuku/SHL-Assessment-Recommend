import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle



print(" Initializing SHL Recommender...")

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load corpus and FAISS index
with open("app/models/corpus.pkl", "rb") as f:
    corpus = pickle.load(f)

index = faiss.read_index("app/models/faiss_index.bin")

print(f" Model and FAISS index loaded successfully! ({len(corpus)} items)")




def get_recommendations(query, top_k=10):
    """Given a query, return top_k most relevant SHL assessments (URLs)."""
    query_vector = model.encode([query])
    query_vector = np.array(query_vector).astype("float32")

    # Search FAISS index
    distances, indices = index.search(query_vector, top_k)

    # Get matched items
    results = [corpus[i] for i in indices[0]]
    
    # Filter URLs only (SHL product links)
    urls = [r for r in results if "https://www.shl.com" in r]
    
    return urls[:top_k]


if __name__ == "__main__":
    print("\n Example Test Queries:\n")
    sample_queries = [
        "Hiring for Python developers with teamwork skills",
        "Need assessment for sales executives with communication skills",
        "Looking for an HR manager test focusing on leadership and behavior"
    ]

    for q in sample_queries:
        print(f"\n Query: {q}")
        results = get_recommendations(q, top_k=5)
        for i, url in enumerate(results, 1):
            print(f"{i}. {url}")
