import streamlit as st
import sqlite3
import pandas as pd

st.title("🏆 Top Companies Ranking")

conn = sqlite3.connect("nifty100.db")

query = """
SELECT
    company_id,
    roe,
    opm
FROM financial_ratios
ORDER BY roe DESC
LIMIT 20
"""

df = pd.read_sql(query, conn)

st.dataframe(
    df,
    use_container_width=True
)

conn.close()