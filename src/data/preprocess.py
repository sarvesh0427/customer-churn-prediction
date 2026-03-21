import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # fixing only required columm
    if "customerID" in df.columns:
        df.drop(columns=["customerID"], inplace=True)
    df.reset_index(drop=True, inplace=True)

    return df