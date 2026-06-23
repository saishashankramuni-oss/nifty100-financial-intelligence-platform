import sqlite3

conn = sqlite3.connect("nifty100.db")

cursor = conn.cursor()

cursor.execute("""
ALTER TABLE financial_ratios
ADD COLUMN roce REAL
""")

conn.commit()

print("ROCE Column Added")

conn.close()