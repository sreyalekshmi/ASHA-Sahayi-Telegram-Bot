import sqlite3

conn = sqlite3.connect("asha_data.db")
cur = conn.cursor()

cur.execute("DELETE FROM patient_visits")
cur.execute("DELETE FROM followups")

conn.commit()
conn.close()

print("🗑️ Database cleared")
