import streamlit as st


def about():

    st.title("About This Project")

    st.markdown("""
    ### 🚀 Customer Churn Prediction System

    This is a **production-ready end-to-end Machine Learning system** that predicts whether a telecom customer is likely to **churn** or stay.

    It is designed to help businesses **identify high-risk customers early** and take proactive retention actions.

    ---

    ### 🎯 Objectives

    - Predict customer churn using ML models  
    - Identify key churn-driving factors  
    - Provide probability-based risk scoring  
    - Build a real-world deployable ML system  
    - Demonstrate full ML lifecycle (data → model → API → frontend)

    ---

    ### ⚙️ Machine Learning Pipeline

    - Data Cleaning & Preprocessing  
    - Feature Engineering (including tenure groups)  
    - Handling Class Imbalance  
    - Model Training (Logistic Regression, Random Forest)  
    - Hyperparameter Tuning (GridSearchCV)  
    - Model Evaluation (ROC-AUC, F1 Score, Accuracy)  
    - Feature Importance Analysis  
    - Model Serialization (Joblib)  

    ---

    ### 🧠 Final Model

    - **Algorithm:** Random Forest Classifier  
    - **ROC-AUC Score:** ~0.86  
    - Tuned using cross-validation  
    - Handles class imbalance effectively  
    - Integrated into production pipeline  

    ---
    """)

    st.subheader("📊 Model Comparison")

    st.table({
        "Model": ["Logistic Regression", "Random Forest"],
        "ROC-AUC": [0.8621, 0.8638]
    })

    st.markdown("""
    ---

    ### 🌐 Deployment Architecture

    - **Frontend:** Streamlit  
    - **Backend:** FastAPI (REST API)  
    - **Model Serving:** Deployed ML pipeline  
    - **Integration:** API-based communication (HTTP requests)  

    ---

    ### 🔗 Live Links

    - 🌍 **Frontend App:** _[https://customer-churn-prediction-ccp.streamlit.app/]_
    - ⚡ **API Endpoint:** _[https://customer-churn-prediction-ccbq.onrender.com]_  
    - 💻 **GitHub Repo:** _[https://github.com/sarvesh0427/customer-churn-prediction]_  

    ---

    ### 🧪 How to Use

    1. Enter customer details in the input form  
    2. Click **Predict Churn Risk**  
    3. System sends request to deployed API  
    4. API returns prediction & probability  
    5. View risk level: Low / Medium / High  

    ---

    ### 💼 Business Impact

    - Detect high-risk customers early  
    - Improve retention strategies  
    - Reduce churn rate  
    - Increase customer lifetime value  
    - Support data-driven decision making  

    ---

    ### 🛠 Tech Stack

    - Python  
    - Scikit-learn  
    - Pandas / NumPy  
    - Matplotlib  
    - FastAPI  
    - Streamlit  
    - Joblib  

    ---

    ### 📌 Key Highlights

    - Full-stack ML system (Frontend + Backend + Model)  
    - REST API deployment (industry practice)  
    - Real-time prediction system  
    - Clean modular architecture  
    - End-to-end ML lifecycle implemented  

    ---

    ### 👨‍💻 Author

    Developed as a **portfolio-level Machine Learning project** demonstrating real-world deployment, API integration, and ML engineering skills.
    """)
