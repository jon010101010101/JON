import pandas as pd
import os


def load(path: str):
    """
    Load a CSV dataset from the specified path and return it as a pandas
    DataFrame.

    Parameters:
    path (str): The path to the CSV file to be loaded.

    Returns:
    pd.DataFrame or None: The loaded dataset as a pandas DataFrame, or
    None if there was an error.

    This function loads a CSV dataset from the given path using the
    pandas library.
    It prints the dimensions of the loaded dataset and returns the
    dataset as a DataFrame.
    If there is an error (e.g., bad path, bad format), None is returned.
    """
    try:
        if not path.lower().endswith('.csv'):
            raise ValueError("The file format is not .csv.")
        if not os.path.exists(path):
            raise FileNotFoundError("The path is bad.")
        df = pd.read_csv(path)

        df = df.loc[:, :'2050']
        return df
    except (FileNotFoundError, ValueError) as error:
        print(type(error).__name__ + ":", error)
        exit()
