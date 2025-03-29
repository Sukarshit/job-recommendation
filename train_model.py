import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Sample training data (You can replace this with real job data)
data = pd.DataFrame({
    'skills': [
        'Python, Flask, SQL',
        'React, JavaScript, CSS',
        'Data Science, ML, Python',
        'Java, Spring Boot, MySQL',
        'DevOps, Docker, Kubernetes'
    ],
    'category': ['Backend', 'Frontend', 'Data Science', 'Backend', 'DevOps']
})

# Vectorizing the skills data
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['skills'])
y = data['category']

# Train a simple model (Random Forest)
model = RandomForestClassifier()
model.fit(X, y)

# Save model and vectorizer
joblib.dump(model, 'models/job_recommender.pkl')
joblib.dump(vectorizer, 'models/vectorizer.pkl')

print("✅ Model and vectorizer saved successfully!")
