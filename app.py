import streamlit as st
import pandas as pd

from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from matcher import calculate_match_score, compare_skills
from recommendations import generate_recommendations


# Page configuration
st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="🤖",
    layout="wide"
)


# Application title
st.title("🤖 AI Resume Screening & Job Matching System")

st.write(
    "Upload a resume and enter a job description to analyze "
    "skills, calculate an AI-powered match score, and receive "
    "personalized recommendations."
)


# Input section
left_column, right_column = st.columns(2)


with left_column:
    st.subheader("📄 Upload Resume")

    resume_file = st.file_uploader(
        "Upload your resume PDF",
        type=["pdf"]
    )


with right_column:
    st.subheader("💼 Job Description")

    job_description = st.text_area(
        "Paste the job description here",
        height=250,
        placeholder=(
            "Example: We are looking for an AI/ML Engineer "
            "with Python, Machine Learning, SQL and Data Science skills..."
        )
    )


# Analyze button
if st.button("🔍 Analyze Resume", use_container_width=True):

    if resume_file is None:
        st.warning("Please upload a resume PDF.")

    elif not job_description.strip():
        st.warning("Please enter a job description.")

    else:

        with st.spinner("Analyzing resume..."):

            # Extract resume text
            resume_text = extract_text_from_pdf(resume_file)

            if not resume_text:
                st.error(
                    "Could not extract text from this PDF. "
                    "Please upload a text-based PDF."
                )
                st.stop()

            # Extract skills
            resume_skills = extract_skills(resume_text)
            job_skills = extract_skills(job_description)

            # Calculate ML similarity
            match_score = calculate_match_score(
                resume_text,
                job_description
            )

            # Compare skills
            matched_skills, missing_skills = compare_skills(
                resume_skills,
                job_skills
            )

            # Generate recommendations
            recommendations = generate_recommendations(
                missing_skills
            )


        # Results
        st.divider()

        st.header("📊 Resume Analysis Results")


        # Main metrics
        score_column, matched_column, missing_column = st.columns(3)


        with score_column:
            st.metric(
                "🎯 Match Score",
                f"{match_score}%"
            )


        with matched_column:
            st.metric(
                "✅ Matched Skills",
                len(matched_skills)
            )


        with missing_column:
            st.metric(
                "❌ Missing Skills",
                len(missing_skills)
            )


        # Match score progress bar
        st.subheader("📈 Job Match")

        st.progress(
            min(int(match_score), 100)
        )


        # Skill Analysis Chart
        st.subheader("📊 Skill Analysis")

        skill_data = pd.DataFrame({
            "Category": [
                "Resume Skills",
                "Job Skills",
                "Matched Skills",
                "Missing Skills"
            ],
            "Count": [
                len(resume_skills),
                len(job_skills),
                len(matched_skills),
                len(missing_skills)
            ]
        })

        st.bar_chart(
            skill_data.set_index("Category")
        )


        # Matched skills
        st.subheader("✅ Matched Skills")

        if matched_skills:

            for skill in matched_skills:
                st.success(skill.title())

        else:
            st.info("No matching skills detected.")


        # Missing skills
        st.subheader("❌ Missing Skills")

        if missing_skills:

            for skill in missing_skills:
                st.error(skill.title())

        else:

            st.success(
                "No missing skills detected from the supported skill list."
            )


        # AI recommendations
        st.subheader("💡 AI Recommendations")

        if recommendations:

            for item in recommendations:

                st.info(
                    f"**{item['skill']}** — "
                    f"{item['recommendation']}"
                )

        else:

            st.success(
                "Great! No additional skills were identified as missing."
            )


        # Resume skills
        st.subheader("🧠 Skills Detected in Resume")

        if resume_skills:

            st.write(
                ", ".join(
                    skill.title()
                    for skill in resume_skills
                )
            )

        else:

            st.info(
                "No supported skills detected."
            )


        # Job description skills
        st.subheader("💼 Skills Detected in Job Description")

        if job_skills:

            st.write(
                ", ".join(
                    skill.title()
                    for skill in job_skills
                )
            )

        else:

            st.info(
                "No supported skills detected."
            )


        # Extracted resume text
        with st.expander("📄 View Extracted Resume Text"):

            st.text(resume_text)


        # Download Analysis Report
        st.subheader("📥 Download Analysis Report")

        report = f"""
AI RESUME SCREENING & JOB MATCHING SYSTEM
==========================================

RESUME ANALYSIS RESULTS
-----------------------

Match Score: {match_score}%

Matched Skills ({len(matched_skills)}):
{", ".join(skill.title() for skill in matched_skills)}

Missing Skills ({len(missing_skills)}):
{", ".join(skill.title() for skill in missing_skills)}

Resume Skills:
{", ".join(skill.title() for skill in resume_skills)}

Job Description Skills:
{", ".join(skill.title() for skill in job_skills)}

AI RECOMMENDATIONS
------------------

"""

        for item in recommendations:
            report += (
                f"{item['skill']}: "
                f"{item['recommendation']}\n"
            )


        st.download_button(
            label="📄 Download Analysis Report",
            data=report,
            file_name="resume_analysis_report.txt",
            mime="text/plain"
        )