# Customer Churn Analysis using SQL (PostgreSQL)

## Project Overview
This project demonstrates a full data pipeline within a SQL environment using a Telecommunications dataset. The goal is to identify why customers are leaving (churning) and provide actionable insights for retention strategies.

I transitioned the raw CSV data into a **PostgreSQL** database via **pgAdmin 4**, performed deep data cleaning, and executed complex queries to understand churn drivers.


## Tech Stack
* **Database:** PostgreSQL 18
* **Interface:** pgAdmin 4
* **Languages:** SQL
* **Key Skills:** Table Schema Design, Data Type Casting, CTEs, Window Functions, and Feature Engineering.

## Project Structure
The project is divided into four modular SQL scripts:
1. `01_table_setup.sql`: Defines the database schema and constraints.
2. `02_data_cleaning.sql`: Handles null values and converts `TotalCharges` from text to numeric.
3. `03_exploratory_eda.sql`: Queries for churn rates, contract analysis, and revenue impact.
4. `04_feature_eng.sql`: Transforms categorical data into numerical flags (0/1) for ML readiness.

## Key Findings & Insights
Using SQL, I uncovered several high-impact insights:

* **Contract Type:** Customers on **Month-to-month** contracts are **15x more likely** to churn than those on Two-year contracts.
* **Monthly Charges:** Churned customers have an average monthly charge of **$74.44**, which is significantly higher than the **$61.26** average for loyal customers.
* **High Risk Segment:** Fiber Optic users on month-to-month plans represent the highest risk category for the business.


## How to Setup
1. **Create Database:** Open pgAdmin 4 and create a database named `telecom_db`.
2. **Execute Setup:** Run the code in `sql_scripts/01_table_setup.sql`.
3. **Import Data:** - Right-click the `customer_churn` table -> **Import/Export Data**.
   - Select `raw_data.csv`.
   - Under **Options**, set `Header` to `Yes`.
4. **Run Pipeline:** Execute scripts `02` through `04` in sequence to clean and analyze the data.

## Future Work: Machine Learning
The final script (`04_feature_eng.sql`) generates a view specifically formatted for Machine Learning. This data can be exported to Python for building predictive models like Logistic Regression or Random Forest to automate churn detection.

---
