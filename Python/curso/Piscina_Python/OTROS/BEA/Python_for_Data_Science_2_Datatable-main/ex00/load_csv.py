import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV DataFrame from the specified path and return it as a pandas
    DataFrame.

    Parameters:
    path (str): The path to the CSV file to be loaded.

    Returns:
    pd.DataFrame: The loaded DataFrame as a pandas DataFrame.

    This function loads a CSV DataFrame from the given path using the
    pandas library.
    DataFrame as a DataFrame.
    If there is an error (e.g., bad path, bad format), it prints the error
    message and does not return anything.
    """
    try:
        if not path.lower().endswith('.csv'):
            raise ValueError("The file format is not .csv.")
        if not os.path.exists(path):
            raise FileNotFoundError("The path is bad.")
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        # Load the CSV and set the country as index
        df = pd.read_csv(path, index_col="country")
        return df

    except (FileNotFoundError, ValueError) as error:
        print(type(error).__name__ + ":", error)
        return None
