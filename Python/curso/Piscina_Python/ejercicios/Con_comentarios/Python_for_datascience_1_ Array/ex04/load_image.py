from PIL import Image  # Importar la biblioteca PIL para la manipulación de imágenes
import numpy as np  # Importar numpy para trabajar con arreglos
import os  # Importar os para verificar la existencia del archivo

def ft_load(path: str) -> np.ndarray:
    """
    Carga una imagen y devuelve su contenido de píxeles en formato RGB.

    Parámetros:
    path (str): La ruta al archivo de imagen.

    Retorna:
    np.ndarray: Los datos de píxeles de la imagen en formato RGB.

    Excepciones:
    ValueError: Si el formato de la imagen no es compatible o si hay un problema
    al cargar la imagen.
    """
    # Verificar si la ruta existe
    if not os.path.exists(path):
        raise ValueError(f"Error: La ruta '{path}' no existe.")

    try:
        # Cargar la imagen desde la ruta especificada
        image = Image.open(path)
        # Asegurarse de que la imagen esté en formato RGB
        image = image.convert('RGB')
        # Convertir la imagen a un arreglo de numpy
        pixels = np.array(image)
        return pixels  # Retornar los datos de píxeles en formato RGB

    except IOError:
        raise ValueError(
            f"Error: No se puede cargar la imagen en '{path}'. "
            "Por favor, verifica la ruta y el formato del archivo."
        )
    except Exception as e:
        raise ValueError(f"Ocurrió un error inesperado: {e}")


