import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

query = """
SELECT
    company_id,
    roe,
    opm
FROM financial_ratios
ORDER BY roe DESC
LIMIT 20
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()