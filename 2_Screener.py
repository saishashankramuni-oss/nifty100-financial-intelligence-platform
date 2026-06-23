import streamlit as st
import sqlite3
import pandas as pd

st.title("Investment Screener")

conn = sqlite3.connect("nifty100.db")

query = """
SELECT *
FROM financial_ratios
WHERE roe > 15
AND debt_to_equity < 1
AND opm > 10
"""

df = pd.read_sql(query, conn)

st.dataframe(df)

conn.close()