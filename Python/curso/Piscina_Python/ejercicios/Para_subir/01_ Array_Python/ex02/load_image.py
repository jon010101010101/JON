from PIL import Image
import numpy as np
import os
import sys


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image, prints its shape and pixel content in RGB format.

    Parameters:
    path (str): The path to the image file.

    Returns:
    np.ndarray: The pixel data of the image in RGB format.
    """
    try:
        # Check if the file format is jpg or jpeg
        _, ext = os.path.splitext(path)
        if ext.lower() not in ['.jpg', '.jpeg']:
            print("Error: The file must be in JPG or JPEG format.")
            sys.exit(1)  # Termina el programa con código de salida 1

        # Check if the file exists
        if not os.path.isfile(path):
            print(f"Error: The file '{path}' does not exist.")
            sys.exit(1)  # Termina el programa con código de salida 1

        # Load the image
        image = Image.open(path)

        # Ensure the image is in RGB format
        image = image.convert('RGB')

        # Convert the image to a numpy array
        pixels = np.array(image)

        # Print the shape of the image (dimensions and color channels)
        print(f"The shape of the image is: {pixels.shape}")

        return pixels  # Return the pixel data in RGB format

    except Exception:
        print("Error: An unexpected error occurred while loading the image.")
        sys.exit(1)  # Termina el programa con código de salida 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python load_image.py <image_path>")
        sys.exit(1)  # Termina el programa con código de salida 1

    image_path = sys.argv[1]
    ft_load(image_path)
