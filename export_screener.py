import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

query = """
SELECT *
FROM financial_ratios
WHERE roe > 15
"""

df = pd.read_sql(query, conn)

df.to_csv(
    "output/screener_results.csv",
    index=False
)

print("Export Completed")

conn.close()