import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(
    page_title="Investment Screener",
    layout="wide"
)

st.title("🔍 Investment Screener")

conn = sqlite3.connect("nifty100.db")

query = """
SELECT
    company_id,
    year,
    roe,
    opm,
    debt_to_equity
FROM financial_ratios
WHERE
    roe > 15
    AND opm > 10
    AND debt_to_equity < 1
ORDER BY roe DESC
"""

df = pd.read_sql(query, conn)

st.dataframe(
    df,
    use_container_width=True
)

st.write("Total Companies Found:", len(df))

conn.close()