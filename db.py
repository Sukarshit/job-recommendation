import psycopg2

def connect_db():
    conn = psycopg2.connect(
        database="job_recommendation",
        user="postgres",
        password="yourpassword",
        host="localhost",
        port="5432"
    )
    return conn
