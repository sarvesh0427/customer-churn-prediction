import joblib
from pathlib import Path
from typing import Any


def save_object(obj: Any, filepath: str) -> None:
    path = Path(filepath)

    # create directory if it doesn't exist
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        joblib.dump(obj, path)
        print(f"Object saved successfully at {filepath}")

    except Exception as e:
        raise RuntimeError(f"Error saving object: {e}")


def load_object(filepath: str) -> Any:
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"Error... File not found at: {filepath}")
    try:
        obj = joblib.load(path)
        print(f"Object loaded from: {filepath}")
        return obj

    except Exception as e:
        raise RuntimeError(f"Error!!! Failed to load object: {e}")