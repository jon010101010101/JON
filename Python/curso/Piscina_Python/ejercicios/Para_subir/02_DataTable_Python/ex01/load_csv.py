import pandas as pd
import os


def load_csv(path: str) -> pd.DataFrame:
    """
    Loads the CSV file and returns a DataFrame.

    Parameters:
    path (str): The path to the CSV file to be loaded.

    Returns:
    pd.DataFrame: The loaded DataFrame, or None if there's an error.
    """

    # Check if the file format is .csv
    if not path.lower().endswith('.csv'):
        print("Error: The file format is not .csv.")
        return None  # Return None if the format is incorrect

    # Check if the file exists
    if not os.path.exists(path):
        print("Error: The file does not exist or the path is incorrect.")
        return None  # Return None if the file does not exist

    try:
        # Load the CSV file
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data

    except Exception as e:
        print(f"Error loading the file: {str(e)}")
        return None
