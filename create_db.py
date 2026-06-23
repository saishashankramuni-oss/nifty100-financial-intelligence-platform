import sqlite3

conn = sqlite3.connect("nifty100.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS companies (
    id TEXT PRIMARY KEY,
    company_name TEXT,
    website TEXT,
    face_value REAL,
    book_value REAL,
    roce_percentage REAL,
    roe_percentage REAL
)
""")

conn.commit()

print("Companies Table Created")

conn.close()