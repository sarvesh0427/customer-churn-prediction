from src.data.load_data import load_data
from src.data.preprocess import clean_data
from src.features.build_features import create_features, split_features_target
from src.models.train_model import train_model
from src.models.evaluate import evaluate_model
from src.utils.helpers import save_object

DATA_PATH = "data/clean_data.csv"
MODEL_PATH = "models/churn_model.pkl"
FEATURE_PATH = "models/feature_columns.pkl"


def run_training():
    print("Starting training pipeline...")

    # load data
    df = load_data(DATA_PATH)

    # Clean data
    df = clean_data(df)
    # feature engineering
    df = create_features(df)
    # split features and target
    X, y = split_features_target(df)

    print(f"Dataset ready: {X.shape[0]} rows, {X.shape[1]} features")

    # Train model
    model, X_test, y_test = train_model(X, y)

    # evaluate model
    evaluate_model(model, X_test, y_test)
    # save model
    save_object(model, MODEL_PATH)

    # Save feature columns (VERY IMPORTANT)
    save_object(X.columns.tolist(), FEATURE_PATH)
    print("Training pipeline completed successfully!")


if __name__ == "__main__":
    run_training()