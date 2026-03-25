from src.data.load_data import load_data
from src.data.preprocess import clean_data
from src.features.build_features import create_features, split_features_target
from src.features.preprocessor import build_preprocessor
from src.models.train_model import train_model
from src.models.evaluate import evaluate_model
from src.utils.helpers import save_object


DATA_PATH = "data/clean_data.csv"
MODEL_PATH = "models/final_pipeline.pkl"


def run_training():
    print("...Starting training pipeline...")

    # Load data
    df = load_data(DATA_PATH)

    # Clean data
    df = clean_data(df)
    # Feature engineering
    df = create_features(df)

    # Splitting features and target 
    X, y =split_features_target(df)

    print(f'Dataset ready: {X.shape[0]} rows, {X.shape[1]} features')

    # Build preprocessor
    numerical_features = X.select_dtypes(include=["int64", "float64"]).columns
    categorical_features = X.select_dtypes(include=["object"]).columns

    preprocessor = build_preprocessor(numerical_features, categorical_features)

    # Train model
    model, X_test, y_test = train_model(X, y, preprocessor)

    # Evaluate model
    metrics = evaluate_model(model, X_test, y_test)

    print(f"Model Accuracy: {metrics['accuracy']}")
    print(f"ROC-AUC: {metrics['roc_auc']}")
    print("Classification Report:\n ", metrics["report"])

    # save full pipeline
    save_object(model, MODEL_PATH)
    print("Training pipeline completed successfully!")


if __name__ == "__main__":
    run_training()