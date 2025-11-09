from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

app = Flask(__name__)

# ===============================
# LOAD MODEL AND INDEX
# ===============================
print("🚀 Starting Flask API...")

model = SentenceTransformer('all-MiniLM-L6-v2')
with open("app/models/corpus.pkl", "rb") as f:
    corpus = pickle.load(f)
index = faiss.read_index("app/models/faiss_index.bin")

print(f"✅ Model & Index Loaded: {len(corpus)} items available.")


# ===============================
# ROUTES
# ===============================
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "OK",
        "message": "API is running"
    }), 200


@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    if not data or "query" not in data:
        return jsonify({"error": "Missing 'query' field in JSON"}), 400

    query = data["query"]
    query_vector = model.encode([query])
    query_vector = np.array(query_vector).astype("float32")

    # Search
    distances, indices = index.search(query_vector, 10)
    results = [corpus[i] for i in indices[0]]
    urls = [r for r in results if "https://www.shl.com" in r][:10]

    return jsonify({
        "query": query,
        "recommendations": [{"assessment_url": url} for url in urls]
    })


# ===============================
# RUN SERVER
# ===============================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
