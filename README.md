Absolutely ✅ Sairam — here’s a clean, professional **`README.md`** ready for your GitHub repo.

It’s written exactly how SHL expects:

* Concise but detailed
* Includes your project purpose, setup, API docs, and deployment details
* Perfect for evaluation and submission

---

## 🧠 `README.md` (copy this into your file)

```markdown
# 🧠 SHL Assessment Recommendation System

### Developed by **Panuku Sairam**
> Submission for SHL AI Research Intern Challenge 2025  

---

## 🚀 Overview

Hiring managers often struggle to identify the most relevant SHL assessments for specific job roles.  
This project builds a **Generative AI-based Recommendation System** that intelligently maps job descriptions or queries to SHL’s assessment catalog using **semantic retrieval (RAG)**.

---

## 🎯 Objective

Given a **natural language job query or JD**, the system recommends **5–10 relevant SHL individual test solutions** (ignoring pre-packaged solutions).

Example:
> **Input:** “Hiring for Java developers with teamwork and communication skills.”  
> **Output:** A ranked list of relevant SHL assessment URLs (e.g., Java technical test + communication skills test).

---

## 🧩 Tech Stack

| Layer | Technology |
|-------|-------------|
| Frontend | Streamlit |
| Backend API | Flask |
| Embeddings | Sentence Transformers (`all-MiniLM-L6-v2`) |
| Vector DB | FAISS |
| Language | Python |
| Deployment | Render (API) + Streamlit Cloud (Web App) |

---

## ⚙️ Features

✅ Takes natural language job queries or JD text  
✅ Retrieves most relevant SHL assessments (5–10)  
✅ Balanced results (technical + behavioral)  
✅ Simple web UI for testing  
✅ API endpoints for automated evaluation  
✅ Uses modern LLM-based RAG approach  

---

## 🧠 System Architecture

```

[ User Query ]
↓
Sentence Transformer (Embeddings)
↓
FAISS Vector Store (Similarity Search)
↓
Relevant SHL Assessment URLs
↓
Flask API  →  Streamlit Frontend

````

---

## 🧪 API Endpoints

### 🔹 `/health`  
**GET** → Check server status  
**Response:**
```json
{ "status": "OK", "message": "API is running" }
````

### 🔹 `/recommend`

**POST** → Get assessment recommendations
**Input (JSON):**

```json
{ "query": "Hiring for Java developer with teamwork and communication skills" }
```

**Output (JSON):**

```json
{
  "query": "Hiring for Java developer with teamwork and communication skills",
  "recommendations": [
    {"assessment_url": "https://www.shl.com/solutions/products/product-catalog/view/core-java-advanced-level-new/"},
    {"assessment_url": "https://www.shl.com/solutions/products/product-catalog/view/global-skills-assessment/"}
  ]
}
```

---

## 🧰 Local Setup Instructions

### 1️⃣ Clone this repository

```bash
git clone https://github.com/Sairam-Panuku/SHL-Assessment-Recommend.git
cd SHL-Assessment-Recommend
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the backend Flask API

```bash
python app/main.py
```

Access it at → [http://127.0.0.1:5000/health](http://127.0.0.1:5000/health)

### 5️⃣ Run the Streamlit frontend

```bash
streamlit run webapp/app.py
```

Open → [http://localhost:8501](http://localhost:8501)

---

## ☁️ Deployment (for SHL submission)

| Component          | Platform        | Example URL                                                 |
| ------------------ | --------------- | ----------------------------------------------------------- |
| Flask API          | Render          | `https://shl-api.onrender.com`                              |
| Streamlit Frontend | Streamlit Cloud | `https://shl-recommender.streamlit.app`                     |
| GitHub Repo        | GitHub          | `https://github.com/Sairam-Panuku/SHL-Assessment-Recommend` |

---

## 📁 Directory Structure

```
shl_assessment_recommender/
│
├── app/
│   ├── data/
│   │   └── train_data.xlsx
│   ├── main.py          ← Flask API
│   ├── recommender.py   ← Embeddings + FAISS logic
│
├── webapp/
│   └── app.py           ← Streamlit frontend
│
├── requirements.txt
├── README.md
└── notebooks/
    └── data_exploration.ipynb
```

---

## 🧾 Evaluation Metrics

* **Mean Recall@10** for test queries
* Balanced results across multiple assessment categories
* Functional API + accessible web frontend

---

## 🏁 Final Notes

* This system uses SHL’s public product catalog for recommendations.
* It demonstrates a scalable, explainable RAG-based architecture for assessment recommendation.

> **Status:** ✅ Ready for SHL evaluation

---

**Developed by:**
👨‍💻 *Panuku Sairam*
📧 [sairampanuku123@gmail.com](mailto:sairampanuku123@gmail.com)
🌐 [LinkedIn](https://www.linkedin.com/in/sairam-panuku)

````


