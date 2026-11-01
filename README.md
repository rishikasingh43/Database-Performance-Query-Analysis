# Database Performance & Query Analysis Tool

A Python-based web application built with Streamlit to execute SQL queries, analyze database records, and measure query execution time. The tool helps users explore employee data, perform SQL operations, and understand basic database query performance.

## Features

- **Dashboard:** Displays total employee records and number of departments.
- **SQL Query Analyzer:** Execute SQL queries and view the results.
- **Execution Time Measurement:** Measures and displays query execution time in milliseconds.
- **Sample SQL Queries:** Includes predefined queries for common database operations.
- **Department Analysis:** Analyze employee distribution and salary information across departments.
- **Data Visualization:** Presents database analysis through visual charts and tables.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| SQLite | Database management |
| SQL | Query execution and data analysis |
| Pandas | Data handling and analysis |
| Matplotlib | Data visualization |

## Project Structure

```text
Database-Performance-Query-Analysis-Project/
│
├── app.py              # Main Streamlit application
├── performance.db      # Local SQLite database
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignored files
└── README.md           # Project documentation
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/rishikasingh43/Database-Performance-Query-Analysis.git
```

### 2. Navigate to the Project Directory

```bash
cd Database-Performance-Query-Analysis
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

`http://localhost:8501`

## Example SQL Queries

**Retrieve all employees**

```sql
SELECT * FROM employees;
```

**Filter employees by department**

```sql
SELECT * FROM employees
WHERE department = 'IT';
```

**Find the highest salary**

```sql
SELECT * FROM employees
ORDER BY salary DESC
LIMIT 1;
```

**Calculate average salary by department**

```sql
SELECT department, AVG(salary)
FROM employees
GROUP BY department;
```

## Application Screenshots

Screenshots of the dashboard, SQL Query Analyzer, and Department Analysis can be added here.

## Learning Outcomes

- Practical understanding of SQL queries and database operations.
- Experience building interactive applications using Streamlit.
- Understanding query execution time measurement.
- Working with structured data and database analysis.

## Author

**Rishika Singh**

BCA Graduate | Python | SQL | Data Analysis

GitHub: https://github.com/rishikasingh43
