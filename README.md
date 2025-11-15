Resume Screening System Using NLP
Project Overview

This project is an ATS-style Resume Screening System built using Natural Language Processing (NLP) techniques.
It allows recruiters or HR professionals to automatically screen and rank resumes based on their similarity to a job description.

The system supports:

Uploading multiple resumes in PDF format

Comparing them with a Job Description (JD)

Generating an ATS Score (%) for each resume

Ranking resumes from best to least match

Visualizing results with progress bars and charts

Saving the ranked results to a CSV file

Technologies Used

Python – main programming language

PyPDF2 – extract text from PDF resumes

scikit-learn – TF-IDF vectorizer & cosine similarity

Pandas – data handling & CSV export

Matplotlib – visualization of similarity scores

Streamlit – web frontend for uploading resumes and displaying ATS results

Regex – text preprocessing and cleaning

Project Features

Extract text from multiple PDF resumes

Clean and preprocess resumes & job description

Convert text into numerical features using TF-IDF

Compute similarity between JD and resumes using cosine similarity

Generate ATS Score (%) for each resume

Display ranked results in a table

Visualize scores with bar charts

Save results to CSV for HR record keeping

Simple and interactive Streamlit frontend

Usage Instructions
1. Clone the Repository
git clone <your-repo-link>
cd Resume-Screening-NLP

2. Install Dependencies
pip install -r requirements.txt


Required Libraries:

streamlit

PyPDF2

scikit-learn

pandas

matplotlib

3. Run the Streamlit App
streamlit run app.py


Paste the Job Description in the text area

Upload one or multiple PDF resumes

View ATS Score (%) for each resume

Download ranked results as CSV

Project Structure
Resume-Screening-NLP/
│
├── app.py                   # Streamlit frontend + ML logic
├── model/                   # Optional: save trained TF-IDF vectorizer
├── resumes/                 # Folder containing resume PDFs
├── jds/                     # Folder containing job description text files
├── requirements.txt         # Python dependencies
├── ATS_Resume_Scores.csv    # Output CSV file
└── README.md                # Project documentation
