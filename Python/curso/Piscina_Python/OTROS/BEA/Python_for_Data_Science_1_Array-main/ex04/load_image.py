from PIL import Image
import numpy as np
import os


def ft_load(path):
    """
    Load the image and return its array representation.

    Parameters:
    path (str): The path to the image file.

    Returns:
    numpy.ndarray: The array representation of the image.

    This function loads the image from the specified path using PIL
    and returns its array representation using NumPy.
    """
    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        if not os.path.exists(path):
            raise AssertionError("File not found:", path)
        img = Image.open(path)
        print(
            f"The shape of the image is ({img.size[1]}, {img.size[0]}, 1) or "
            f"({img.size[1]}, {img.size[0]})"
        )
        return np.array(img)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        return ""
