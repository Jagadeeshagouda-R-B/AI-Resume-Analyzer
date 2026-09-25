import re


SKILLS = [
    "python",
    "java",
    "c++",
    "javascript",
    "typescript",
    "html",
    "css",
    "react",
    "node.js",
    "express",
    "mongodb",
    "mysql",
    "sql",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "nlp",
    "computer vision",
    "opencv",
    "data science",
    "data analysis",
    "power bi",
    "tableau",
    "git",
    "github",
    "docker",
    "aws",
    "azure",
]


def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    return sorted(found_skills)