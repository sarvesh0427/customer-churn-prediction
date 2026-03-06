-- Create the initial raw table
CREATE TABLE IF NOT EXISTS raw_data (
    customerID VARCHAR(20) primary key,
    gender VARCHAR(10),
    SeniorCitizen INT,
    Partner VARCHAR(5),
    Dependents VARCHAR(5),
    tenure INT,
    PhoneService VARCHAR(5),
    MultipleLines VARCHAR(20),
    InternetService VARCHAR(20),
    OnlineSecurity VARCHAR(20),
    OnlineBackup VARCHAR(20),
    DeviceProtection VARCHAR(20),
    TechSupport VARCHAR(20),
    StreamingTV VARCHAR(20),
    StreamingMovies VARCHAR(20),
    Contract VARCHAR(20),
    PaperlessBilling VARCHAR(5),
    PaymentMethod VARCHAR(50),
    MonthlyCharges NUMERIC(10, 2),
    TotalCharges VARCHAR(20), 
    Churn VARCHAR(5)
);

-- first 10 rows
select * from raw_data limit 10;

-- calculate churn rate
SELECT Churn, COUNT(*) as Total
FROM raw_data
GROUP BY Churn;