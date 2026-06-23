import pandas as pd
import sqlite3

df = pd.read_excel(
    "data/raw/prosandcons.xlsx",
    header=1
)

conn = sqlite3.connect("nifty100.db")

df.to_sql(
    "prosandcons",
    conn,
    if_exists="replace",
    index=False
)

print("Pros & Cons Loaded")
print("Rows:", len(df))

conn.close()