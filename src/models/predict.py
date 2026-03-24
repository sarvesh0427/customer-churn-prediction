import joblib
import numpy as np

def load_model(path: str):
    try:
        model = joblib.load(path)
        print(f'Model loaded from {path}')
        return model
    except Exception as e:
        raise RuntimeError(f"Error...Failed to load model: {e}")


def predict(model, data):
    try:
        prediction = model.predict(data)
        return prediction
    except Exception as e:
        raise RuntimeError(f"Error!!!Prediction failed: {e}")


def predict_proba(model, data):
    try:
        proba = model.predict_proba(data)
        return proba
    
    except Exception as e:
        raise RuntimeError(f'Error!!!Probability prediction failed: {e}')