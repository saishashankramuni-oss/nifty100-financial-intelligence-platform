import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

query = """
SELECT *
FROM profitandloss
WHERE company_id='ADANIPORTS'
ORDER BY year
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()