from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import joblib
import pandas as pd

app = FastAPI()

# templates + static
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# load model
model = joblib.load("../models/churn_model.pkl")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
def predict(
    request: Request,
    tenure: float = Form(...),
    MonthlyCharges: float = Form(...),
    TotalCharges: float = Form(...)
):
    # minimal example (you can add all features later)
    data = {
        "tenure": tenure,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges,
        "gender": "Male",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "No",
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "Yes",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "Yes",
        "StreamingMovies": "Yes",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check"
    }

    df = pd.DataFrame([data])
    prob = model.predict_proba(df)[0][1]

    if prob > 0.7:
        risk = "High Risk"
    elif prob > 0.4:
        risk = "Medium Risk"
    else:
        risk = "Low Risk"

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "prob": round(prob * 100, 2),
            "risk": risk
        }
    )
