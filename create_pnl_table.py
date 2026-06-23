import sqlite3

conn = sqlite3.connect("nifty100.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS profitandloss (
    id INTEGER,
    company_id TEXT,
    year TEXT,
    sales REAL,
    expenses REAL,
    operating_profit REAL,
    opm_percentage REAL,
    other_income REAL,
    interest REAL,
    depreciation REAL,
    profit_before_tax REAL,
    tax_percentage REAL,
    net_profit REAL,
    eps REAL,
    dividend_payout REAL
)
""")

conn.commit()

print("Profit and Loss Table Created")

conn.close()