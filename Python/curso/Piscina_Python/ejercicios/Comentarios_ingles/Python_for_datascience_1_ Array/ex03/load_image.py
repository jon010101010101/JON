from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image, prints its shape and pixel content in RGB format.

    Parameters:
    path (str): The path to the image file.

    Returns:
    np.ndarray: The pixel data of the image in RGB format.

    Raises:
    ValueError: If the image format is not supported or if there is
     an issue loading the image.
    """
    try:
        # Load the image
        image = Image.open(path)

        # Ensure the image is in RGB format
        image = image.convert('RGB')

        # Convert the image to a numpy array
        pixels = np.array(image)

        # Print the shape of the image (dimensions and color channels)
        print(f"The shape of the image is: {pixels.shape}")

        return pixels  # Return the pixel data in RGB format

    except FileNotFoundError:
        raise ValueError(
            f"Error: No se puede encontrar el archivo '{path}'. "
            "Por favor, verifica la ruta."
        )
    except ValueError as e:
        raise e
    except Exception as e:
        raise ValueError(f"Error inesperado al cargar la imagen: {e}")
