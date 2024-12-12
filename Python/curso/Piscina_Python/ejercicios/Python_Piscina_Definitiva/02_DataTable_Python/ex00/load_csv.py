import pandas as pd
import os
import sys


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV DataFrame from the specified path and return
     it as a pandas DataFrame.

    Parameters:
    path (str): The path to the CSV file to be loaded.

    Returns:
    pd.DataFrame: The loaded DataFrame as a pandas DataFrame.

    If there is an error (e.g., bad path, bad format), it prints
     the error message and exits the program.
    """
    try:
        # Check if the file format is .csv
        if not path.lower().endswith('.csv'):
            raise ValueError("The file format is not .csv.")

        # Check if the file exists
        if not os.path.exists(path):
            raise FileNotFoundError(
                "The file does not exist or "
                "the path is incorrect."
            )

        # Load the CSV without setting index first to check columns
        df = pd.read_csv(path)

        # Print the dimensions of the loaded dataset
        print(f"Loading dataset of dimensions {df.shape}")

        # Load the CSV and set the country as index
        df = pd.read_csv(path, index_col="country")
        return df

    except (FileNotFoundError, ValueError) as error:
        print(f"{type(error).__name__}: {error}")
        sys.exit(1)
