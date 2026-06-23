import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

df = pd.read_sql(
    "SELECT * FROM growth_metrics LIMIT 20",
    conn
)

print(df)

conn.close()