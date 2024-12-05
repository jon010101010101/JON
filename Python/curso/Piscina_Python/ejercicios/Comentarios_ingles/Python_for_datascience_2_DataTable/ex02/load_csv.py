import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    """
    Loads the CSV file and returns a DataFrame.

    Parameters:
    path (str): The path to the CSV file to be loaded.

    Returns:
    pd.DataFrame: The loaded DataFrame.
    None: If there is an error loading the file.
    """
    try:
        if not path.lower().endswith('.csv'):
            raise ValueError("The file format is not .csv.")

        if not os.path.exists(path):
            raise FileNotFoundError(
                "The file does not exist or "
                "the path is incorrect."
            )

        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        print(data.head())
        return data

    except Exception as e:
        print(f"{type(e).__name__}: {str(e)}")
        return None
