import sqlite3

conn = sqlite3.connect("nifty100.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS financial_ratios (
    company_id TEXT,
    year TEXT,
    opm REAL,
    net_profit_margin REAL,
    roe REAL,
    debt_to_equity REAL,
    operating_cashflow_ratio REAL
)
""")

conn.commit()

print("financial_ratios table created")

conn.close()