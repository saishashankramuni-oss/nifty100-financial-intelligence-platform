import pandas as pd
import sqlite3

# Read Excel file
df = pd.read_excel(
    "data/raw/companies.xlsx",
    header=1
)

# Connect database
conn = sqlite3.connect("nifty100.db")

# Select required columns
df = df[
    [
        "id",
        "company_name",
        "website",
        "face_value",
        "book_value",
        "roce_percentage",
        "roe_percentage"
    ]
]

# Insert into database
df.to_sql(
    "companies",
    conn,
    if_exists="replace",
    index=False
)

print("Companies Loaded Successfully")
print("Rows Loaded:", len(df))

conn.close()