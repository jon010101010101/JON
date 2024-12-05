import numpy as np
from PIL import Image
import os
import sys


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image, prints its information and returns the pixel data.

    Parameters:
    path (str): The path to the image file.

    Returns:
    np.ndarray: The pixel data of the image in RGB format.
    """
    try:
        # Check if the file format is jpg or jpeg first
        if not path.lower().endswith(('.jpg', '.jpeg')):
            raise ValueError("The file must be in JPG or JPEG format.")

        # Check if the file exists
        if not os.path.isfile(path):
            raise FileNotFoundError(f"The file '{path}' does not exist.")

        # Load the image
        image = Image.open(path)
        pixels = np.array(image)

        # Print image information
        # Size in pixels (height, width, channels)
        print(f"The shape of the image is: {pixels.shape}")
        print(f"Number of channels: {pixels.shape[2]}")  # Number of channels
        print("Pixel content of the image (first 3x3 pixels):")
        print(pixels[:3, :3])  # Print pixel content (first 3x3 area)

        return pixels

    except (ValueError, FileNotFoundError) as e:
        print(f"Error: {str(e)}")  # Simplified error message
        sys.exit(1)
    except Exception:
        print("Error: An unexpected error occurred while loading the image.")
        sys.exit(1)
