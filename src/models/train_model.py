import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report


def train_model(X, y, preprocessor):

    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=42,stratify=y)

    model = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("classifier", RandomForestClassifier(
            n_estimators=200,max_depth=8,
            min_samples_split=5,
            class_weight='balanced',
            random_state=42
        ))
    ])
    print("model training...")
    model.fit(X_train, y_train)

    # Evaluationn of model
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {acc:.4f}')
    print("Classification Report:\n", classification_report(y_test, y_pred))
    return model, X_test, y_test


def save_model(model, path):
    joblib.dump(model, path)
    print(f"Model saved to {path}")