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

@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    tenure: int = Form(...),
    monthly_charges: float = Form(...)
):
    input_data = {
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
        # add all other features with default values for now
    }

    df = pd.DataFrame([input_data])
    df = df.reindex(columns=feature_names)

    prediction = model.predict(df)
    result = "Customer Will Churn ❌" if prediction[0] == 1 else "Customer Will Stay ✅"

    return templates.TemplateResponse(
        "result.html",
        {"request": request, "result": result}
    )