import pandas as pd
import sqlite3

df = pd.read_excel(
    "data/raw/balancesheet.xlsx",
    header=1
)

conn = sqlite3.connect("nifty100.db")

df.to_sql(
    "balancesheet",
    conn,
    if_exists="replace",
    index=False
)

print("Balance Sheet Loaded")
print("Rows:", len(df))

conn.close()