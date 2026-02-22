import os
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import pickle

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

model = pickle.load(open(os.path.join(BASE_DIR, "models", "churn_model.pkl"), "rb"))

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    tenure: int = Form(...),
    monthly_charges: float = Form(...)
):
    prediction = model.predict([[tenure, monthly_charges]])
    result = "Customer Will Churn ❌" if prediction[0] == 1 else "Customer Will Stay ✅"

    return templates.TemplateResponse(
        "result.html",
        {"request": request, "result": result}
    )