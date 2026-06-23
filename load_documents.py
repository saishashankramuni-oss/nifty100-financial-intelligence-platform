import pandas as pd
import sqlite3

df = pd.read_excel(
    "data/raw/documents.xlsx",
    header=1
)

conn = sqlite3.connect("nifty100.db")

df.to_sql(
    "documents",
    conn,
    if_exists="replace",
    index=False
)

print("Documents Loaded")
print("Rows:", len(df))

conn.close()