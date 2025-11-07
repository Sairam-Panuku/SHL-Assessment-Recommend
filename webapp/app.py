import streamlit as st
import requests
import pandas as pd

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

    .css-1q8dd3e {
        color: white !important;
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


with st.container():
    st.markdown("<div class='main'>", unsafe_allow_html=True)

    st.title("🧠 SHL Assessment Recommendation System")
    st.markdown(
        "### Helping recruiters find the perfect SHL assessments for any job description or hiring query."
    )

    query = st.text_area(
        " Enter your Job Description or Hiring Query",
        placeholder="e.g., Hiring for Java developers with teamwork and problem-solving skills",
    )

    api_url = "http://127.0.0.1:5000/recommend"

    if st.button(" Get Recommendations"):
        if not query.strip():
            st.warning("Please enter a query first.")
        else:
            with st.spinner("Fetching recommendations from SHL Recommender..."):
                try:
                    response = requests.post(api_url, json={"query": query})
                    if response.status_code == 200:
                        data = response.json()
                        recs = data.get("recommendations", [])
                        if recs:
                            st.success(f" Found {len(recs)} recommendations:")
                            df = pd.DataFrame(recs)
                            st.markdown("<div class='recommend-table'>", unsafe_allow_html=True)
                            st.table(df)
                            st.markdown("</div>", unsafe_allow_html=True)
                        else:
                            st.warning("No recommendations found. Try a different query.")
                    else:
                        st.error(f"Error {response.status_code}: Unable to fetch results.")
                except Exception as e:
                    st.error(f" Could not connect to API: {e}")

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
