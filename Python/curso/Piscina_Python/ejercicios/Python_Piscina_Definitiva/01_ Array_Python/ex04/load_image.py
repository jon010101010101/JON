from PIL import Image  # Import the PIL library for image manipulation
import numpy as np  # Import numpy for working with arrays
import os  # Import os to check the existence of the file


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image and returns its pixel content in RGB format.

    Parameters:
    path (str): The path to the image file.

    Returns:
    np.ndarray: The pixel data of the image in RGB format.

    Exceptions:
    ValueError: If the image format is not supported or if there is an issue
    loading the image.
    """

    # Check if the file format is jpg or jpeg
    _, ext = os.path.splitext(path)
    if ext.lower() not in ['.jpg', '.jpeg']:
        raise ValueError("Error: The file must be in JPG or JPEG format.")

    # Check if the file exists
    if not os.path.exists(path):
        raise ValueError(f"Error: The path '{path}' does not exist.")

    try:
        # Load the image
        image = Image.open(path)
        # Ensure the image is in RGB format
        image = image.convert('RGB')
        # Convert the image to a numpy array
        pixels = np.array(image)
        return pixels  # Return the pixel data in RGB format

    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {e}")
