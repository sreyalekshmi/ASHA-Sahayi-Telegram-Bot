import sqlite3
from datetime import datetime

DB_NAME = "asha_data.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS visits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        asha_id TEXT,
        patient_name TEXT,
        patient_age INTEGER,
        patient_location TEXT,
        symptoms TEXT,
        advice TEXT,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()

def log_visit(asha_id, patient_name, patient_age, patient_location, symptoms, advice):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO visits 
    (asha_id, patient_name, patient_age, patient_location, symptoms, advice, timestamp)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        asha_id,
        patient_name,
        patient_age,
        patient_location,
        symptoms,
        advice,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()
