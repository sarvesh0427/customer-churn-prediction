import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("models/churn_model.pkl")
feature_names = joblib.load("models/feature_names.pkl")

st.set_page_config(
    page_title="Customer Churn Predictor",
    layout="centered",
    initial_sidebar_state="expanded"   # keeps sidebar fixed open
)
# Sidebar navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["Home","About"])

if section == 'Home':
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

    if st.button("Predict Churn Risk"):

        prob = model.predict_proba(input_df)[0][1]
        pred = model.predict(input_df)[0]

        st.subheader("Prediction Result")

        st.metric("Churn Probability", f"{prob:.2%}")

        if prob > 0.7:
            st.error("🔴 High Risk Customer — Immediate retention action recommended")
        elif prob > 0.4:
            st.warning("🟡 Medium Risk Customer — Monitor closely")
        else:
            st.success("🟢 Low Risk Customer — Likely to stay")

elif section == "About":
    st.title("About this project")


# ----- FIXED FOOTER -----
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0e1117;
        color: #ffffff;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        border-top: 1px solid #444;
        z-index: 999;
    }
    </style>

    <div class="footer">
        Customer Churn Practice Project
    </div>
    """,
    unsafe_allow_html=True
)


