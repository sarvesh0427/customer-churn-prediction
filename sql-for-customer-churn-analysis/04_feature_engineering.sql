-- Create a table specifically for Machine Learning input
CREATE TABLE churn_ml_features AS
SELECT 
    customerID,
    -- Convert Binary Categories to 0/1
    CASE WHEN gender = 'Male' THEN 1 ELSE 0 END as is_male,
    SeniorCitizen,
    CASE WHEN Partner = 'Yes' THEN 1 ELSE 0 END as has_partner,
    CASE WHEN Dependents = 'Yes' THEN 1 ELSE 0 END as has_dependents,
    CASE WHEN PaperlessBilling = 'Yes' THEN 1 ELSE 0 END as paperless,
    
    -- Label Encoding for Contract
    CASE 
        WHEN Contract = 'Month-to-month' THEN 0 
        WHEN Contract = 'One year' THEN 1 
        WHEN Contract = 'Two year' THEN 2 
    END as contract_rank,
    
    -- One-Hot Encoding for Internet Service
    CASE WHEN InternetService = 'Fiber optic' THEN 1 ELSE 0 END as has_fiber,
    CASE WHEN InternetService = 'DSL' THEN 1 ELSE 0 END as has_dsl,
    
    -- Keep Numerical columns
    tenure,
    MonthlyCharges,
    TotalCharges,
    
    -- Target Variable
    CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END as target_churn
FROM v_churn_clean;

-- Preview the ML-ready data
SELECT * FROM churn_ml_features LIMIT 10;