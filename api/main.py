from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

from src.utils.helpers import load_object
from src.features.build_features import create_features

# Load model
MODEL_PATH = "models/final_pipeline.pkl"
model = load_object(MODEL_PATH)

app = FastAPI(title="Customer Churn Prediction API")


# Input schema
class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float


def create_tenure_group(df):
    df["tenure_group"] = df["tenure"] // 12
    return df

@app.get("/")
def home():
    return {"message": "Churn Prediction API is running"}


@app.post("/predict")
def predict(data: CustomerData):
    try:
        input_df = pd.DataFrame([data.dict()])

        input_df = create_tenure_group(input_df)

        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0][1]

        return {
            "churn_prediction": int(prediction),
            "churn_probability": float(probability)
        }

    except Exception as e:
        return {"error": str(e)}