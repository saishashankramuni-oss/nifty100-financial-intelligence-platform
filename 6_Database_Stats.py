import streamlit as st
import sqlite3
import pandas as pd

st.title("🗄 Database Statistics")

conn = sqlite3.connect("nifty100.db")

tables = [
    "companies",
    "profitandloss",
    "balancesheet",
    "cashflow",
    "analysis",
    "documents",
    "prosandcons",
    "financial_ratios",
    "growth_metrics"
]

stats = []

for table in tables:

    try:

        count = pd.read_sql(
            f"SELECT COUNT(*) as cnt FROM {table}",
            conn
        )

        stats.append(
            {
                "Table": table,
                "Rows": count.iloc[0]["cnt"]
            }
        )

    except:
        pass

stats_df = pd.DataFrame(stats)

st.dataframe(
    stats_df,
    use_container_width=True
)

conn.close()