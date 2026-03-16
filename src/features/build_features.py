import pandas as pd


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # create tenure group 
    if "tenure" in df.columns:
        df["tenure_group"] = df["tenure"] // 12

    # convert target variable churn to numeric
    if "Churn" in df.columns:
        df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    # encode categorical features
    categorical_cols = df.select_dtypes(include=["object"]).columns

    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    return df


def split_features_target(df: pd.DataFrame, target_column: str = "Churn"):
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return X, y