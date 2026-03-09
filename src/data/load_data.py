import pandas as pd

def load_data(filepath: str):
    df = pd.read_csv(filepath)
    return df