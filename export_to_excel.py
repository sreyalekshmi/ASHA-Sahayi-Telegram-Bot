import sqlite3
import pandas as pd

conn = sqlite3.connect("asha_data.db")

visits_df = pd.read_sql_query("SELECT * FROM patient_visits", conn)
followups_df = pd.read_sql_query("SELECT * FROM followups", conn)

visits_df.to_excel("asha_visits.xlsx", index=False)
followups_df.to_excel("asha_followups.xlsx", index=False)

conn.close()

print("✅ Excel files created successfully!")
