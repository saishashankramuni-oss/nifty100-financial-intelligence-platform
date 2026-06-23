import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

query = """
SELECT
    company_id,
    year,
    COUNT(*) as cnt
FROM profitandloss
GROUP BY company_id, year
HAVING COUNT(*) > 1
ORDER BY company_id, year
"""

df = pd.read_sql(query, conn)

print(df)

df.to_csv(
    "output/dq02_duplicates.csv",
    index=False
)

conn.close()