import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


def train_model(X, y, preprocessor):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )
    model = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("classifier", RandomForestClassifier(
            n_estimators=200,
            max_depth=8,
            min_samples_split=5,
            class_weight="balanced",
            random_state=42
        ))
    ])

    model.fit(X_train, y_train)

    return model, X_test, y_test

# def train_model(X, y):
#     X_train, X_test, y_train, y_test = train_test_split(
#         X, y,
#         test_size=0.2,
#         random_state=42,
#     )

#     model = RandomForestClassifier(
#         n_estimators=100,
#         random_state=42
#     )

#     model.fit(X_train, y_train)
#     return model, X_test, y_test


def save_model(model, path):
    joblib.dump(model, path)    # save trained model
    print(f"Model saved to {path}")