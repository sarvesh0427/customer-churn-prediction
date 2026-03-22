import pandas as pd

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # tenure group
    if "tenure" in df.columns:
        df['tenure_group'] = df["tenure"] //12
    # fixing target column
    if "Churn" in df.columns:
        df["Churn"] = df['Churn'].astype(str).str.strip().str.lower()

        # handle multiple formats
        df["Churn"] = df["Churn"].map({ 'yes': 1, "no ": 0,"1": 1, "0": 0})

        # check before dropping
        print('Unique values after mapping:', df["Churn"].unique())
        df = df[df["Churn"].notna()]

    return df

def split_features_target(df: pd.DataFrame, target_column: str = "Churn"):
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return X, y