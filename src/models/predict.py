import joblib


def load_model(path):

    model = joblib.load(path)

    return model


def predict(model, data):

    prediction = model.predict(data)

    return prediction