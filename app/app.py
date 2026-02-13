import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("models/churn_model.pkl")
feature_names = joblib.load("models/feature_names.pkl")

st.set_page_config(page_title="Customer Churn Predictor", layout="centered")

st.title("Customer Churn Prediction")
st.write("Enter customer details to predict churn risk.")

# input fields

gender = st.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
tenure = st.slider("Tenure (months)", 0, 72, 12)
MonthlyCharges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
TotalCharges = st.number_input("Total Charges", 0.0, 10000.0, 1000.0)
Contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

# adding remaining features

# Create dataframe
input_dict = {
    "gender": gender,
    "SeniorCitizen": SeniorCitizen,
    "tenure": tenure,
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": TotalCharges,
    "Contract": Contract,
    "InternetService": InternetService
}

input_df = pd.DataFrame([input_dict])

# Add missing columns safely
for col in feature_names:
    if col not in input_df.columns:
        input_df[col] = None

# Correct order
input_df = input_df[feature_names]

# Fix numeric types
num_cols = ["tenure", "MonthlyCharges", "TotalCharges", "SeniorCitizen"]
for c in num_cols:
    if c in input_df.columns:
        input_df[c] = pd.to_numeric(input_df[c], errors="coerce")


# prediction

if st.button("Predict Churn"):

    prob = model.predict_proba(input_df)[0][1]
    pred = model.predict(input_df)[0]

    st.subheader("Prediction Result")

    if pred == 1:
        st.error(f"Customer likely to churn (Risk: {prob:.2%})")
    else:
        st.success(f"Customer likely to stay (Risk: {prob:.2%})")

    # Risk level
    if prob > 0.7:
        st.write("🔴 High Risk Customer")
    elif prob > 0.4:
        st.write("🟡 Medium Risk Customer")
    else:
        st.write("🟢 Low Risk Customer")
