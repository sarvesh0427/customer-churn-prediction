import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Convert TotalCharges to numeric
    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# remove missing values
    df.dropna(inplace=True)

    # remove duplicate row
    df.drop_duplicates(inplace=True)

    # drop ID column 
    if "customerID" in df.columns:
        df.drop(columns=["customerID"], inplace=True)

    df.reset_index(drop=True, inplace=True)

    return df