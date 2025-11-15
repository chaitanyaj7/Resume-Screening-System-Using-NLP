import streamlit as st
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import pandas as pd

# --- Function to extract text ---
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# --- Function to clean text ---
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

# --- Streamlit UI ---
st.title("📄 ATS Resume Screening System (Using NLP)")
st.write("Upload candidate resumes and paste a Job Description to calculate ATS Match Scores based on TF-IDF similarity.")

# Input JD
jd_text = st.text_area("📋 Paste Job Description Here")

# Upload resumes
uploaded_files = st.file_uploader("📂 Upload Resumes (PDF)", type=["pdf"], accept_multiple_files=True)

if uploaded_files and jd_text:
    jd_clean = clean_text(jd_text)
    resumes_data = {}

    # Extract and clean resume text
    for file in uploaded_files:
        resume_text = extract_text_from_pdf(file)
        resumes_data[file.name] = clean_text(resume_text)

    # Combine all documents (JD + Resumes)
    documents = [jd_clean] + list(resumes_data.values())

    # TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Cosine Similarity
    similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    # Convert to ATS percentage
    ats_scores = [round(score * 100, 2) for score in similarities]

    # Combine names + scores
    results = sorted(zip(resumes_data.keys(), ats_scores), key=lambda x: x[1], reverse=True)
    df = pd.DataFrame(results, columns=["Resume", "ATS_Score (%)"])

    # Display results
    st.subheader("🏆 ATS Resume Ranking Results")
    st.dataframe(df)

    # Show individual resume results with progress bars
    st.subheader("📊 Individual Resume ATS Scores")
    for name, score in results:
        st.write(f"**{name}** — {score}% match")
        st.progress(int(score))

    # Save CSV
    df.to_csv("ATS_Resume_Scores.csv", index=False)
    st.success("✅ Results saved as 'ATS_Resume_Scores.csv'")
