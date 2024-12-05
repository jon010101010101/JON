import pandas as pd
import os
import sys


def load(path):
    """
    Load a CSV file and return a pandas DataFrame.

    Args:
    path (str): Path to the CSV file to be loaded.

    Returns:
    pd.DataFrame: DataFrame with the loaded data.
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
        return data
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
