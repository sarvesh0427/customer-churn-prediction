import os
import joblib
import pandas as pd
import gradio as gr

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

model_path = os.path.join(base_dir, "models", "churn_model.pkl")
feature_path = os.path.join(base_dir, "models", "feature_names.pkl")
default_path = os.path.join(base_dir, "models", 'default_values.pkl')


model = joblib.load(model_path)
feature_names = joblib.load(feature_path)
default_values = joblib.load(default_path)

def predict_churn(tenure, monthly_charges):

    # start from safe default row
    input_data = default_values.copy()

    # override user inputs
    input_data["tenure"] = tenure
    input_data["MonthlyCharges"] = monthly_charges

    df = pd.DataFrame([input_data])
    df = df.reindex(columns=feature_names)

    prob = model.predict_proba(df)[0][1]

    risk = " High Risk" if prob > 0.5 else " Low Risk"

    return f"{prob:.2%}", risk


interface = gr.Interface(

    fn=predict_churn,
    inputs=[
        gr.Number(label="Tenure (months)", value=12),
        gr.Number(label="Monthly Charges ($)", value=70),],

    outputs=[
        gr.Text(label="Churn Probability"),
        gr.Text(label="Risk Level"),
    ],

    title="Customer Churn Prediction",

    description="Enter customer details to predict churn risk.",
)

if __name__ == "__main__":
    interface.launch()