from src.data.load_data import load_data
from src.data.preprocess import clean_data
from src.features.build_features import create_features, split_features_target
from src.models import train_model, evaluate
import joblib

DATA_PATH = "data/clean_data.csv"
MODEL_PATH = "models/churn_model.pkl"
FEATURE_PATH = "models/feature_columns.pkl"


def run_training():
    print("Starting training pipeline...")
    # 1.load data
    df = load_data(DATA_PATH)

    # 2. Clean data
    df = clean_data(df)

    # 3. feature engineering
    df = create_features(df)

    # 4. split features and target
    X, y = split_features_target(df)
    # 5. Train model
    model, X_test, y_test = train_model(X, y)

    # 6. Evaluate model
    evaluate(model, X_test,y_test)

    # 7. Save model
    # save_model(model,MODEL_PATH)
    # 8. Save feature columns
    joblib.dump(X.columns.tolist(), FEATURE_PATH)
    print(f"Feature columns saved to {FEATURE_PATH}")
    print("Training pipeline completed successfully!")

if __name__ == "__main__":
    run_training()