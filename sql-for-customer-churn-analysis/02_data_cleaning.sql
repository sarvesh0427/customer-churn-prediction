-- fix empty strings in TotalCharges (common for new customers with 0 tenure)
update raw_data 
set TotalCharges = '0' 
where TotalCharges = ' ' or TotalCharges is null;

-- convert TotalCharges to Numeric for analysis
ALTER TABLE raw_data 
ALTER COLUMN TotalCharges TYPE NUMERIC(10,2) 
USING TotalCharges::numeric;

-- standardize text data (Optional: ensures no trailing spaces)
UPDATE raw_data SET 
    gender = TRIM(gender),
    Contract = TRIM(Contract),
    Churn = TRIM(Churn);

-- Create a Cleaned View for easier querying
CREATE VIEW v_churn_clean AS
SELECT * FROM raw_data;