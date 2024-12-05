from PIL import Image
import numpy as np
import os


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image, prints its shape and pixel content in RGB format.

    Parameters:
    path (str): The path to the image file.

    Returns:
    np.ndarray: The pixel data of the image in RGB format.

    Exceptions:
    ValueError: If the image format is not supported, if the file
    doesn't exist, or if there is an issue loading the image.
    """
    try:
        # Check if the file exists
        if not os.path.isfile(path):
            raise ValueError(
                f"Error: The file '{path}' does not exist."
            )

        # Check if the file format is jpg or jpeg
        _, ext = os.path.splitext(path)
        if ext.lower() not in ['.jpg', '.jpeg']:
            raise ValueError(
                "Error: The file must be in JPG or JPEG format."
            )

        # Load the image
        image = Image.open(path)

        # Ensure the image is in RGB format
        image = image.convert('RGB')

        # Convert the image to a numpy array
        pixels = np.array(image)

        # Print the shape of the image (dimensions and color channels)
        print(f"The shape of the image is: {pixels.shape}")

        return pixels  # Return the pixel data in RGB format

    except ValueError as ve:
        # Re-raise ValueError for specific checks we've added
        raise ve
    except IOError:
        # If there is an error loading the image, raise a ValueError
        raise ValueError(
            f"Error: Cannot load the image at '{path}'. "
            "Please check the path and file format."
        )
    except Exception as e:
        # For any other unexpected error, also raise a ValueError
        raise ValueError(f"An unexpected error occurred: {e}")
