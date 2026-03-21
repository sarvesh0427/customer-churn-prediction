import pandas as pd
from pathlib import Path


def load_data(filepath: str) -> pd.DataFrame:

    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found at: {filepath}")

    try:
        df = pd.read_csv(path, encoding="utf-8")
        print(f"Dataset loaded successfully from {filepath}")
        print(f"Shape: {df.shape}")
        return df

    except Exception as e:
        raise RuntimeError(f"error loading dataset: {e}")