import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Dummy Job Dataset
jobs = [
    {"id": 1, "title": "Software Engineer", "skills": "Python, Flask, React"},
    {"id": 2, "title": "Data Scientist", "skills": "Python, ML, Deep Learning"},
    {"id": 3, "title": "Frontend Developer", "skills": "React, CSS, HTML"},
    {"id": 4, "title": "Backend Developer", "skills": "Node.js, Express, MongoDB"},
]

df = pd.DataFrame(jobs)

def recommend_jobs(user_skills):
    if not user_skills:
        print("⚠️ No skills provided!")
        return []  # Return an empty list
    
    try:
        print(f"🔍 Matching skills: {user_skills}")

        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(df["skills"])
        user_vector = vectorizer.transform([user_skills])
        similarity = cosine_similarity(user_vector, tfidf_matrix)[0]

        # Get indices sorted by similarity scores
        indices = similarity.argsort()[-3:][::-1]  

        # Ensure indices match dataframe length
        indices = [i for i in indices if i < len(df)]  

        print(f"✅ Recommended Jobs: {df.iloc[indices].to_dict(orient='records')}")
        return df.iloc[indices].to_dict(orient="records")

    except Exception as e:
        print(f"❌ Error in recommend_jobs: {str(e)}")
        return []
