from src.data.load_data import load_data
from src.data.preprocess import clean_data
from src.features.build_features import create_features
from src.models.train_model import train_model, save_model

DATA_PATH = "data/raw/customer_churn.csv"
MODEL_PATH = "models/churn_model.pkl"


def run_training():

    df = load_data(DATA_PATH)

    df = clean_data(df)

    df = create_features(df)

    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    model, X_test, y_test = train_model(X, y)

    save_model(model, MODEL_PATH)


if __name__ == "__main__":
    run_training()