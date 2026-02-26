import gradio as gr
import joblib
import pandas as pd
import os

# go to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# load model
model = joblib.load(
    os.path.join(BASE_DIR, "models", "churn_model.pkl")
)

feature_names = joblib.load(
    os.path.join(BASE_DIR, "models", "feature_names.pkl")
)


def predict_churn(tenure, monthly_charges):

    input_data = {
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
    }

    df = pd.DataFrame([input_data])

    df = df.reindex(columns=feature_names, fill_value=0)

    prob = model.predict_proba(df)[0][1]

    if prob > 0.7:
        risk = "High Risk ❌"
    elif prob > 0.4:
        risk = "Medium Risk ⚠"
    else:
        risk = "Low Risk ✅"

    return f"Churn Probability: {prob*100:.2f}% | {risk}"


app = gr.Interface(
    fn=predict_churn,
    inputs=[
        gr.Number(label="Tenure (months)"),
        gr.Number(label="Monthly Charges"),
    ],
    outputs="text",
    title="Customer Churn Prediction",
    description="ML model using Scikit-learn Pipeline"
)

app.launch()