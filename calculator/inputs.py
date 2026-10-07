"""Read a CSV input source; choosing and performing math belong elsewhere."""
from pathlib import Path
import pandas as pd


def read_csv_values(path, column="value"):
    frame = pd.read_csv(Path(path))

    # modified for independent task in part 5

    if column not in frame.columns:
        raise ValueError(f"CSV must contain a column named {column}.")
    return frame[column].tolist()

    