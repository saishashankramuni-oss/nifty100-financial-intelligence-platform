import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(
    page_title="Sector Analysis",
    layout="wide"
)

st.title("📊 Sector Analysis")

conn = sqlite3.connect("nifty100.db")

# Read sectors table
sectors = pd.read_sql(
    """
    SELECT *
    FROM sectors
    """,
    conn
)

st.subheader("Sector Data")

st.dataframe(
    sectors,
    use_container_width=True
)

# Sector Counts
if "sector" in sectors.columns:

    st.subheader("Companies per Sector")

    sector_count = (
        sectors["sector"]
        .value_counts()
    )

    st.bar_chart(sector_count)

conn.close()