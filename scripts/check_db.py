import sqlite3

conn = sqlite3.connect("storage/database/careerpilot.db")

cursor = conn.cursor()

print("\n===== TABLES =====")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

print("\n===== RESUMES =====")
cursor.execute("SELECT * FROM resumes;")
rows = cursor.fetchall()

print(f"Total Rows: {len(rows)}")

for row in rows:
    print(row)

conn.close()