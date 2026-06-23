import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

tables = [
    "companies",
    "profitandloss",
    "balancesheet",
    "cashflow",
    "analysis",
    "documents",
    "prosandcons"
]

audit_data = []

for table in tables:
    query = f"SELECT COUNT(*) FROM {table}"
    count = pd.read_sql(query, conn).iloc[0, 0]

    audit_data.append({
        "table_name": table,
        "rows_loaded": count
    })

audit_df = pd.DataFrame(audit_data)

audit_df.to_csv(
    "output/load_audit.csv",
    index=False
)

print(audit_df)

conn.close()