import streamlit as st
import pandas as pd
import requests


def home():
    st.title("Customer Churn Prediction")
    st.write("Enter customer details to predict churn risk.")

    st.header("Customer Information")

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
        Partner = st.selectbox("Partner", ["Yes", "No"])
        Dependents = st.selectbox("Dependents", ["Yes", "No"])
        tenure = st.slider("Tenure (Months)", 0, 72, 12)

    with col2:
        PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
        MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
        InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
        Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
        PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])

    st.header("Charges")

    MonthlyCharges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
    TotalCharges = st.number_input("Total Charges", 0.0, 10000.0, 1000.0)

    st.header("Services")

    OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
    StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
    PaymentMethod = st.selectbox("Payment Method",
        ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])


    # adding remaining features

    input_dict = {
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }


    input_df = pd.DataFrame([input_dict])


    # prediction
    API_URL = "https://customer-churn-prediction-ccbq.onrender.com"

    if st.button("Predict Churn Risk"):

        try:
            response = requests.post(API_URL, json=input_dict)

            if response.status_code == 200:
                result = response.json()
                # st.write(response.json())

                pred = result["churn_prediction"]
                prob = result["churn_probability"]

                st.subheader("Prediction Result")
                st.metric("Churn Probability", f"{prob:.2%}")

                if prob > 0.7:
                    st.error("High Risk Customer — Immediate retention action recommended")
                elif prob > 0.4:
                    st.warning("Medium Risk Customer — Monitor closely")
                else:
                    st.success("Low Risk Customer — Likely to stay")

            else:
                st.error(f"API Error: {response.text}")

        except Exception as e:
            st.error(f"Connection Error: {e}")

