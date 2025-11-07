import streamlit as st
import pandas as pd
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer


st.set_page_config(
    page_title="SHL Assessment Recommender",
    page_icon="🧠",
    layout="wide",
)


st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #2b5876, #4e4376);
        font-family: 'Segoe UI', sans-serif;
        color: #ffffff;
    }
    .main {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(12px);
        border-radius: 20px;
        padding: 40px 60px;
        margin: 40px auto;
        width: 75%;
        color: #fff;
        box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.15);
    }
    h1 {
        text-align: center;
        font-size: 2.3em;
        color: #f2f2f2;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    }
    .stButton>button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border-radius: 10px;
        font-weight: 600;
        transition: 0.3s;
        border: none;
        box-shadow: 0px 3px 8px rgba(0,0,0,0.3);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #764ba2, #667eea);
        transform: scale(1.05);
    }
    .footer {
        text-align: center;
        color: #ddd;
        font-size: 0.9em;
        margin-top: 50px;
    }
    .recommend-table {
        background-color: rgba(255,255,255,0.1);
        border-radius: 12px;
        padding: 10px;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_resource(show_spinner=True)
def load_model():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    with open("app/models/corpus.pkl", "rb") as f:
        corpus = pickle.load(f)
    index = faiss.read_index("app/models/faiss_index.bin")
    return model, corpus, index

model, corpus, index = load_model()
st.success(" Model and FAISS index loaded successfully!")


def get_recommendations(query, top_k=10):
    query_vector = model.encode([query])
    query_vector = np.array(query_vector).astype("float32")
    distances, indices = index.search(query_vector, top_k)
    results = [corpus[i] for i in indices[0]]
    urls = [r for r in results if "https://www.shl.com" in r]
    return urls[:top_k]


with st.container():
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.title("🧠 SHL Assessment Recommendation System")
    st.markdown("### Helping recruiters find the perfect SHL assessments for any job description or hiring query.")

    query = st.text_area(
        "Enter your Job Description or Hiring Query",
        placeholder="e.g., Hiring for Java developers with teamwork and problem-solving skills",
    )

    if st.button("Get Recommendations"):
        if not query.strip():
            st.warning("Please enter a query first.")
        else:
            with st.spinner("Finding best SHL assessments..."):
                urls = get_recommendations(query)

                if urls:
                    st.success(f"Found {len(urls)} relevant assessments:")
                    df = pd.DataFrame({"Assessment URL": urls})
                    st.markdown("<div class='recommend-table'>", unsafe_allow_html=True)
                    st.table(df)
                    st.markdown("</div>", unsafe_allow_html=True)
                else:
                    st.error("No recommendations found. Try another query.")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="footer">
        Developed by <b>Panuku Sairam</b> | SHL AI Research Intern Challenge 2025<br>
        <i>Powered by Python • FAISS • Sentence Transformers • Streamlit</i>
    </div>
    """,
    unsafe_allow_html=True,
)
