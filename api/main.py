import os
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import joblib

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "frontend", "app", "static")),
    name="static"
)

templates = Jinja2Templates(
    directory=os.path.join(BASE_DIR, "frontend", "app", "templates")
)

model = joblib.load(
    os.path.join(BASE_DIR, "models", "churn_model.pkl")
)

import pandas as pd

feature_names = joblib.load(
    os.path.join(BASE_DIR, "models", "feature_names.pkl")
)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    tenure: int = Form(...),
    monthly_charges: float = Form(...)
):

    input_data = {
        "SeniorCitizen": 0,
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": tenure * monthly_charges,

        "gender": "Male",
        "Partner": "No",
        "Dependents": "No",
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "DSL",
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
    }

    import pandas as pd
    df = pd.DataFrame([input_data])

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1] * 100

    if probability < 30:
        risk = "Low Risk "
        risk_class = "low"
    elif probability < 60:
        risk = "Medium Risk ⚠"
        risk_class = "medium"
    else:
        risk = "High Risk "
        risk_class = "high"

    return templates.TemplateResponse(
    "result.html",
    {
        "request": request,
        "probability": probability,
        "risk": risk,
        "risk_class": risk_class
    }
)

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "prediction": prediction,
            "probability": round(probability, 2),
            "risk": risk
        }
    )