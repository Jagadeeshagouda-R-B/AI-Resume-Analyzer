from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_match_score(resume_text, job_description):
    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=5000
    )

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    score = round(similarity * 100, 2)

    return score


def compare_skills(resume_skills, job_skills):
    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched_skills = sorted(resume_set.intersection(job_set))
    missing_skills = sorted(job_set - resume_set)

    return matched_skills, missing_skills