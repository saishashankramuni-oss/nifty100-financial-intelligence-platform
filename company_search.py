import sqlite3
import pandas as pd

company = input("Enter Company ID: ")

conn = sqlite3.connect("nifty100.db")

query = f"""
SELECT *
FROM financial_ratios
WHERE company_id = '{company}'
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()