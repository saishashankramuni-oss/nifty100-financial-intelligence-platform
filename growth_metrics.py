import pandas as pd
import sqlite3

conn = sqlite3.connect("nifty100.db")

pnl = pd.read_sql(
    "SELECT company_id, year, sales, net_profit, eps FROM profitandloss",
    conn
)

pnl = pnl.sort_values(
    ["company_id", "year"]
)

pnl["sales_growth"] = (
    pnl.groupby("company_id")["sales"]
    .pct_change()
) * 100

pnl["profit_growth"] = (
    pnl.groupby("company_id")["net_profit"]
    .pct_change()
) * 100

pnl["eps_growth"] = (
    pnl.groupby("company_id")["eps"]
    .pct_change()
) * 100

growth = pnl[
    [
        "company_id",
        "year",
        "sales_growth",
        "profit_growth",
        "eps_growth"
    ]
]

growth.to_sql(
    "growth_metrics",
    conn,
    if_exists="replace",
    index=False
)

print("Growth Metrics Created")
print("Rows:", len(growth))

conn.close()