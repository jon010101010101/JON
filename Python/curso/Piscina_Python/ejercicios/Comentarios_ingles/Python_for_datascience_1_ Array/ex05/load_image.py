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
    np.ndarray: The pixel data of the image in RGB format or None if
     there's an error.
    """
    try:
        # Check if the file format is jpg or jpeg first
        _, ext = os.path.splitext(path)
        if ext.lower() not in ['.jpg', '.jpeg']:
            print("Error: The file must be in JPG or JPEG format.")
            return None

        # Check if the file exists
        if not os.path.isfile(path):
            print(f"Error: Cannot find the file '{path}'.")
            print("Please check the path.")
            return None

        # Load the image
        image = Image.open(path)
        # Ensure the image is in RGB format
        image = image.convert('RGB')
        # Convert the image to a numpy array
        pixels = np.array(image)
        # Print the shape of the image (dimensions and color channels)
        print(f"The shape of the image is: {pixels.shape}")
        return pixels  # Return the pixel data in RGB format
    #excepcion generica
    except Exception as e:
        print(f"Unexpected error while loading the image: {e}")
        return None
    # finally Este bloque se ejecuta siempre, independientemente de si se
    # produjo una excepción o no en el bloque try
    finally:
        # comprueba si pixels no se creó durante la ejecución de la función
        if 'pixels' not in locals():
            # Si pixels no existe, esta línea hace que el programa termine
            #  inmediatamente
            sys.exit(1)

