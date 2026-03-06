-- 1. Overall Churn Rate
SELECT 
    Churn, 
    COUNT(*) as customer_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) as percentage
FROM v_churn_clean
GROUP BY Churn;

-- 2. Churn by Contract Type (High Insight Query)
SELECT 
    Contract, 
    COUNT(*) as total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) as churned_count,
    ROUND(AVG(CASE WHEN Churn = 'Yes' THEN 1.0 ELSE 0.0 END) * 100, 2) as churn_rate
FROM v_churn_clean
GROUP BY Contract
ORDER BY churn_rate DESC;

-- 3. Average charges for Churned vs Non-Churned
SELECT 
    Churn, 
    ROUND(AVG(MonthlyCharges), 2) as avg_monthly_charges,
    ROUND(AVG(tenure), 1) as avg_tenure_months
FROM v_churn_clean
GROUP BY Churn;