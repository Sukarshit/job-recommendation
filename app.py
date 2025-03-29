from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load job dataset
def load_jobs():
    try:
        jobs_df = pd.read_csv("jobs.csv")  # Ensure jobs.csv is present
        jobs_df["combined_skills"] = jobs_df["description"]  # Modify if skills are stored separately
        return jobs_df
    except Exception as e:
        print(f"Error loading jobs: {e}")
        return None

# Job recommendation function
def recommend_jobs(user_skills):
    jobs_df = load_jobs()
    if jobs_df is None:
        return []

    vectorizer = TfidfVectorizer()
    job_vectors = vectorizer.fit_transform(jobs_df["combined_skills"])
    user_vector = vectorizer.transform([" ".join(user_skills)])

    similarity_scores = cosine_similarity(user_vector, job_vectors)[0]
    jobs_df["similarity"] = similarity_scores

    # Sort jobs by similarity, remove duplicates, and get top 5 recommendations
    recommended_jobs = jobs_df.sort_values(by="similarity", ascending=False).drop_duplicates(subset="title")

    return recommended_jobs[["id", "title", "description"]].head(5).to_dict(orient="records")

# API endpoint to handle job recommendations
@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.get_json()
        skills = data.get("skills", "").split(",")
        if not skills or skills == [""]:
            return jsonify({"error": "No skills provided"}), 400

        recommended_jobs = recommend_jobs(skills)
        return jsonify(recommended_jobs), 200
    except Exception as e:
        print(f"Error in recommendation: {e}")
        return jsonify({"error": "Something went wrong!"}), 500

# Health check route
@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"message": "Job Recommendation API is running!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
