import sqlite3

conn = sqlite3.connect("nifty100.db")

cursor = conn.cursor()

cursor.execute("""
DELETE FROM profitandloss
WHERE rowid NOT IN (
    SELECT MIN(rowid)
    FROM profitandloss
    GROUP BY company_id, year
)
""")

conn.commit()

print("Duplicates Removed")

conn.close()