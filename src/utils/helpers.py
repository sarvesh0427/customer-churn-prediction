import joblib


def save_object(obj, filepath):
    joblib.dump(obj, filepath)


def load_object(filepath):

    return joblib.load(filepath)