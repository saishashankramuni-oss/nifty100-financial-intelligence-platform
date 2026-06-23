import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

results = []

# DQ-01 Company ID duplicates
query = """
SELECT COUNT(*)
FROM (
    SELECT id
    FROM companies
    GROUP BY id
    HAVING COUNT(*) > 1
)
"""

count = pd.read_sql(query, conn).iloc[0, 0]

results.append([
    "DQ-01",
    "Company ID Duplicate Check",
    count,
    "PASS" if count == 0 else "FAIL"
])

# DQ-02 Company-Year duplicates
query = """
SELECT COUNT(*)
FROM (
    SELECT company_id, year
    FROM profitandloss
    GROUP BY company_id, year
    HAVING COUNT(*) > 1
)
"""

count = pd.read_sql(query, conn).iloc[0, 0]

results.append([
    "DQ-02",
    "Company-Year Duplicate Check",
    count,
    "PASS" if count == 0 else "FAIL"
])

report = pd.DataFrame(
    results,
    columns=[
        "rule_id",
        "rule_name",
        "violations",
        "status"
    ]
)

print(report)

report.to_csv(
    "output/validation_report.csv",
    index=False
)

conn.close()