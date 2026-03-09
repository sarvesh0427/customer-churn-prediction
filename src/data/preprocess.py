import pandas as pd

def clean_data(df: pd.DataFrame):

    df = df.copy()

    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    df.dropna(inplace=True)

    return df