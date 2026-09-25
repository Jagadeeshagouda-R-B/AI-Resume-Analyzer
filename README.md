# 🤖 AI Resume Screening & Job Matching System

An AI-powered Resume Screening System built using Python and Streamlit. The application analyzes a candidate's resume, compares it with a job description, calculates a match score, identifies missing skills, and provides learning recommendations.

## Features

- Upload Resume (PDF)
- Extract text from resume
- AI Skill Detection
- TF-IDF Job Matching
- Match Score Calculation
- Skill Analysis Chart
- Missing Skill Detection
- AI Recommendations
- Download Analysis Report

## Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- NumPy
- PyPDF2

## Project Structure

- app.py
- resume_parser.py
- skill_extractor.py
- matcher.py
- recommendations.py

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```