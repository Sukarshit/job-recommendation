from app import app, db, Job  # Import the app and db properly

def seed_data():
    with app.app_context():  # Use the app context correctly
        db.session.add(Job(title="Software Engineer", description="Develop software solutions.", skills_required="Python, Flask, SQL"))
        db.session.add(Job(title="Data Scientist", description="Analyze data trends.", skills_required="Python, Pandas, Machine Learning"))
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == "__main__":
    seed_data()
