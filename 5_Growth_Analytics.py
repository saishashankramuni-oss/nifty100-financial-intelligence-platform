import streamlit as st
import sqlite3
import pandas as pd

st.title("📈 Growth Analytics")

conn = sqlite3.connect("nifty100.db")

df = pd.read_sql(
    """
    SELECT *
    FROM growth_metrics
    """,
    conn
)

st.dataframe(
    df,
    use_container_width=True
)

if "sales_growth" in df.columns:

    st.subheader("Sales Growth Trend")

    chart_df = df[
        [
            "year",
            "sales_growth"
        ]
    ].copy()

    chart_df = chart_df.set_index(
        "year"
    )

    st.line_chart(chart_df)

conn.close()