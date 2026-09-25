def generate_recommendations(missing_skills):
    recommendations = []

    learning_resources = {
        "python": "Strengthen Python programming and problem-solving fundamentals.",
        "sql": "Practice SQL queries, joins, subqueries, and database operations.",
        "pandas": "Practice data manipulation and analysis using Pandas.",
        "numpy": "Practice numerical computing and array operations using NumPy.",
        "scikit-learn": "Practice machine learning model training and evaluation with Scikit-learn.",
        "machine learning": "Study supervised and unsupervised machine learning algorithms.",
        "data analysis": "Practice exploratory data analysis and data visualization.",
        "data preprocessing": "Learn data cleaning, missing-value handling, encoding, and feature scaling.",
        "feature engineering": "Practice creating and selecting useful features for ML models.",
        "deep learning": "Learn neural networks and frameworks such as TensorFlow or PyTorch.",
        "nlp": "Study natural language processing and text-processing techniques.",
        "git": "Learn Git and GitHub fundamentals, branching, commits, and collaboration.",
        "streamlit": "Practice building and deploying interactive ML applications with Streamlit."
    }

    for skill in missing_skills:
        recommendation = learning_resources.get(
            skill,
            f"Improve your knowledge of {skill.title()}."
        )

        recommendations.append({
            "skill": skill.title(),
            "recommendation": recommendation
        })

    return recommendations