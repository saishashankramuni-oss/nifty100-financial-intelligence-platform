import pandas as pd
import sqlite3

conn = sqlite3.connect("nifty100.db")

pnl = pd.read_sql(
    "SELECT * FROM profitandloss",
    conn
)

bs = pd.read_sql(
    "SELECT * FROM balancesheet",
    conn
)

cf = pd.read_sql(
    "SELECT * FROM cashflow",
    conn
)

merged = pnl.merge(
    bs,
    on=["company_id", "year"],
    how="inner"
)

merged = merged.merge(
    cf,
    on=["company_id", "year"],
    how="inner"
)

merged["opm"] = (
    merged["operating_profit"]
    / merged["sales"]
) * 100

merged["net_profit_margin"] = (
    merged["net_profit"]
    / merged["sales"]
) * 100

merged["roe"] = (
    merged["net_profit"]
    /
    (
        merged["equity_capital"]
        +
        merged["reserves"]
    )
) * 100

merged["debt_to_equity"] = (
    merged["borrowings"]
    /
    (
        merged["equity_capital"]
        +
        merged["reserves"]
    )
)

merged["operating_cashflow_ratio"] = (
    merged["operating_activity"]
    / merged["sales"]
)

ratios = merged[
    [
        "company_id",
        "year",
        "opm",
        "net_profit_margin",
        "roe",
        "debt_to_equity",
        "operating_cashflow_ratio"
    ]
]

ratios.to_sql(
    "financial_ratios",
    conn,
    if_exists="replace",
    index=False
)

print("Ratios Generated")
print("Rows:", len(ratios))

conn.close()