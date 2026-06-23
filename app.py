import streamlit as st
import sqlite3
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Nifty100 Financial Intelligence Platform",
    layout="wide"
)

st.title("📈 Nifty100 Financial Intelligence Platform")

# Database Connection
conn = sqlite3.connect("nifty100.db")

# Load Company List
companies = pd.read_sql(
    """
    SELECT DISTINCT company_id
    FROM financial_ratios
    ORDER BY company_id
    """,
    conn
)

# Company Dropdown
company = st.selectbox(
    "Select Company",
    companies["company_id"]
)

# Load Selected Company Data
query = f"""
SELECT *
FROM financial_ratios
WHERE company_id = '{company}'
"""

df = pd.read_sql(query, conn)

# KPI Section
st.subheader("📊 Key Performance Indicators")

if not df.empty:

    latest = df.iloc[-1]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "ROE (%)",
            round(float(latest["roe"]), 2)
        )

    with col2:
        st.metric(
            "OPM (%)",
            round(float(latest["opm"]), 2)
        )

    with col3:
        st.metric(
            "Debt / Equity",
            round(float(latest["debt_to_equity"]), 2)
        )

# Financial Ratio Table
st.subheader("📋 Financial Ratios")

st.dataframe(
    df,
    use_container_width=True
)

# ROE Trend
if not df.empty:

    st.subheader("📈 ROE Trend")

    roe_chart = df[["year", "roe"]].copy()

    roe_chart = roe_chart.set_index("year")

    st.line_chart(roe_chart)

# OPM Trend
if not df.empty:

    st.subheader("📈 OPM Trend")

    opm_chart = df[["year", "opm"]].copy()

    opm_chart = opm_chart.set_index("year")

    st.line_chart(opm_chart)

# Download Button
st.subheader("⬇ Download Data")

csv = df.to_csv(index=False)

st.download_button(
    label="Download CSV",
    data=csv,
    file_name=f"{company}_financial_ratios.csv",
    mime="text/csv"
)

conn.close()