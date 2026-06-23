import pandas as pd
import sqlite3

df = pd.read_excel(
    "data/raw/cashflow.xlsx",
    header=1
)

conn = sqlite3.connect("nifty100.db")

df.to_sql(
    "cashflow",
    conn,
    if_exists="replace",
    index=False
)

print("Cash Flow Loaded")
print("Rows:", len(df))

conn.close()