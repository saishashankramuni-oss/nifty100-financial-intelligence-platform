import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

query = """
SELECT id,
COUNT(*) as duplicate_count
FROM companies
GROUP BY id
HAVING COUNT(*) > 1
"""

duplicates = pd.read_sql(query, conn)

print("Duplicate Company IDs")
print(duplicates)

duplicates.to_csv(
    "output/validation_failures.csv",
    index=False
)

conn.close()