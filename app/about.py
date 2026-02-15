import streamlit as st


def about():

    st.title("About This Project")

    st.markdown("""
    ### Customer Churn Prediction System

    This project is an end-to-end Machine Learning application that predicts whether a telecom customer is likely to **churn (leave the service)** or stay with the company.

    The goal of this project is to help businesses identify **high-risk customers early** so they can take proactive retention actions and reduce revenue loss.

    ---

    ### Objectives

    - Predict customer churn using Machine Learning
    - Identify key factors influencing churn
    - Provide churn probability and risk level
    - Build a real-world deployable ML application
    - Demonstrate full ML lifecycle (data → model → deployment)

    ---

    ### Machine Learning Pipeline

    - Data Cleaning & Preprocessing  
    - Feature Engineering  
    - Handling Class Imbalance  
    - Model Training (Logistic Regression, Random Forest)  
    - Hyperparameter Tuning (GridSearchCV)  
    - Model Evaluation (ROC-AUC, F1 Score, Accuracy)  
    - Feature Importance Analysis  
    - Model Serialization (Joblib)  

    ---

    ### Final Model

    - Algorithm: **Random Forest Classifier**
    - Tuned using Cross Validation
    - Final ROC-AUC: **0.86+**
    - Handles class imbalance
    - Production-ready pipeline

    ---

    ### Deployment

    - Built with **Streamlit**
    - Real-time churn prediction
    - Probability-based risk scoring (Low / Medium / High)
    - Interactive Feature Importance visualization

    ---

    ### Business Impact

    This system can help companies:

    - Detect customers likely to churn
    - Understand why customers leave
    - Improve retention strategies
    - Reduce customer acquisition cost
    - Increase long-term revenue

    ---

    ### Tech Stack

    - Python
    - Scikit-learn
    - Pandas / NumPy
    - Matplotlib
    - Streamlit
    - Joblib

    ---

    ### Author

    Developed as a full Machine Learning project for learning, portfolio, and real-world deployment practice.
    """)
