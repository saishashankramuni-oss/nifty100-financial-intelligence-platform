import sqlite3

conn = sqlite3.connect("nifty100.db")

cursor = conn.cursor()

tables = [
    "companies",
    "profitandloss",
    "balancesheet",
    "cashflow",
    "analysis",
    "documents",
    "prosandcons"
]

for table in tables:

    cursor.execute(
        f"SELECT COUNT(*) FROM {table}"
    )

    count = cursor.fetchone()[0]

    print(table, ":", count)

conn.close()