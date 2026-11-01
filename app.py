import sqlite3
import time
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

DB_NAME = "performance.db"

st.set_page_config(
    page_title="Database Performance Analyzer",
    page_icon="📊",
    layout="wide"
)

def connect_db():
    return sqlite3.connect(DB_NAME)

def setup_database():
    with connect_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                salary REAL NOT NULL
            )
        """)
        count = conn.execute(
            "SELECT COUNT(*) FROM employees"
        ).fetchone()[0]

        if count == 0:
            sample = [
                ("Aarav", "IT", 45000),
                ("Priya", "HR", 38000),
                ("Rahul", "Finance", 52000),
                ("Sneha", "IT", 60000),
                ("Aman", "Sales", 35000),
                ("Neha", "HR", 42000),
                ("Karan", "Finance", 55000),
                ("Riya", "IT", 65000),
            ]
            conn.executemany(
                "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
                sample
            )

def run_query(query):
    start = time.perf_counter()
    with connect_db() as conn:
        result = pd.read_sql_query(query, conn)
    elapsed = (time.perf_counter() - start) * 1000
    return result, elapsed

setup_database()

st.title("📊 Database Performance & Query Analysis Tool")
st.caption("Analyze SQL queries, execution time and database records.")

with connect_db() as conn:
    total_records = conn.execute(
        "SELECT COUNT(*) FROM employees"
    ).fetchone()[0]
    departments = conn.execute(
        "SELECT COUNT(DISTINCT department) FROM employees"
    ).fetchone()[0]

c1, c2 = st.columns(2)
c1.metric("Total Records", total_records)
c2.metric("Departments", departments)

st.divider()

st.subheader("🔍 SQL Query Analyzer")

examples = {
    "View all employees": "SELECT * FROM employees",
    "IT department employees": "SELECT * FROM employees WHERE department = 'IT'",
    "Highest salary": "SELECT * FROM employees ORDER BY salary DESC LIMIT 1",
    "Average salary by department": "SELECT department, AVG(salary) AS average_salary FROM employees GROUP BY department",
    "Count employees by department": "SELECT department, COUNT(*) AS employee_count FROM employees GROUP BY department"
}

choice = st.selectbox("Choose a sample SQL query", list(examples.keys()))
query = st.text_area("SQL Query", value=examples[choice], height=100)

if st.button("▶ Execute Query"):
    try:
        if not query.strip().lower().startswith("select"):
            st.error("Only SELECT queries are allowed in the analyzer.")
        else:
            result, elapsed = run_query(query)
            st.success("Query executed successfully!")
            st.metric("Execution Time", f"{elapsed:.3f} ms")
            st.dataframe(result, use_container_width=True)
    except Exception as error:
        st.error(f"Query error: {error}")

st.divider()

st.subheader("📈 Department Analysis")

with connect_db() as conn:
    data = pd.read_sql_query(
        "SELECT department, AVG(salary) AS average_salary FROM employees GROUP BY department",
        conn
    )

if not data.empty:
    fig, ax = plt.subplots()
    ax.bar(data["department"], data["average_salary"])
    ax.set_xlabel("Department")
    ax.set_ylabel("Average Salary")
    ax.set_title("Average Salary by Department")
    st.pyplot(fig)

st.divider()

st.subheader("➕ Add Employee")

with st.form("employee_form"):
    name = st.text_input("Employee Name")
    department = st.selectbox(
        "Department", ["IT", "HR", "Finance", "Sales"]
    )
    salary = st.number_input("Salary", min_value=0.0, step=1000.0)

    submitted = st.form_submit_button("Add Employee")

    if submitted:
        if name.strip():
            with connect_db() as conn:
                conn.execute(
                    "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
                    (name.strip(), department, salary)
                )
            st.success("Employee added successfully!")
            st.rerun()
        else:
            st.warning("Please enter an employee name.")

st.divider()

st.subheader("📋 Employee Database")

with connect_db() as conn:
    employees = pd.read_sql_query(
        "SELECT * FROM employees ORDER BY id",
        conn
    )

st.dataframe(employees, use_container_width=True)

st.caption("Built using Python, SQLite, Streamlit, Pandas and Matplotlib.")