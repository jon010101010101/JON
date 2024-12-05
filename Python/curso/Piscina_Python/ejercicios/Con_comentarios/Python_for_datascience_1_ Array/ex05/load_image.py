# load_image.py: Carga la imagen y la convierte en un arreglo.

import numpy as np
from PIL import Image


def ft_load(ruta_imagen: str) -> np.ndarray:
    """
    Carga una imagen y la convierte en un arreglo de numpy.

    Parámetros:
    ruta_imagen (str): La ruta al archivo de imagen.

    Retorna:
    np.ndarray: Los datos de píxeles de la imagen como un arreglo de numpy.

    Lanza:
    ValueError: Si la imagen no puede ser abierta o convertida.
    """
    try:
        img = Image.open(ruta_imagen)
        img_array = np.array(img)
        print(f"La forma de la imagen es: {img_array.shape}")
        return img_array

    except Exception as e:
        raise ValueError(f"Error al cargar la imagen: {e}")
