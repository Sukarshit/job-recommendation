import sqlite3

# Connect to SQLite
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# ✅ Create jobs table
cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT
)
""")

# ✅ Insert sample jobs
jobs_data = [
    ("Software Engineer", "Develop applications using Python and Django."),
    ("Frontend Developer", "Build UI with React, JavaScript, and CSS."),
    ("Data Scientist", "Analyze data with Python, Machine Learning, and Pandas."),
    ("Backend Developer", "Work with Node.js, Express, and MongoDB for APIs."),
    ("AI Engineer", "Develop AI models using TensorFlow and deep learning."),
]

for title, description in jobs_data:
    cursor.execute("INSERT INTO jobs (title, description) VALUES (?, ?)", (title, description))

# Save and close
conn.commit()
conn.close()
print("✅ Database setup complete!")
