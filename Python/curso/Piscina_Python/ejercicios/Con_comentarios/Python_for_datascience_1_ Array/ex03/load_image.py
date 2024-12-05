from PIL import Image  # Importar la biblioteca PIL para la manipulación de imágenes
import numpy as np  # Importar numpy para trabajar con arreglos

def ft_load(path: str) -> np.ndarray:
    """
    Carga una imagen, imprime su forma y contenido de píxeles en formato RGB.

    Parámetros:
    path (str): La ruta al archivo de imagen.

    Retorna:
    np.ndarray: Los datos de píxeles de la imagen en formato RGB.

    Excepciones:
    ValueError: Si el formato de la imagen no es compatible o si hay un problema
    al cargar la imagen.
    """
    try:
        # Cargar la imagen
        image = Image.open(path)

        # Asegurarse de que la imagen esté en formato RGB
        image = image.convert('RGB')

        # Convertir la imagen a un arreglo de numpy
        pixels = np.array(image)

        # Imprimir la forma de la imagen (dimensiones y canales de color)
        print(f"La forma de la imagen es: {pixels.shape}")
        
        # Imprimir el contenido de los píxeles (primeros píxeles)
        print(f"Contenido de los píxeles (primeros 5 píxeles):\n{pixels[:5]}")  # Imprimir los primeros 5 píxeles

        return pixels  # Retornar los datos de píxeles en formato RGB

    except IOError:
        raise ValueError(
            f"Error: No se puede cargar la imagen en '{path}'. "
            "Por favor, verifica la ruta y el formato del archivo."
        )
    except Exception as e:
        raise ValueError(f"Ocurrió un error inesperado: {e}")

