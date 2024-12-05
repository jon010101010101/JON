
from PIL import Image  # Importamos la librería PIL para manipulación de imágenes
import numpy as np  # Importamos numpy para trabajar con matrices

def ft_load(path: str) -> np.ndarray:
    """
    Carga una imagen, imprime su formato y su contenido de píxeles en formato RGB.

    Parámetros:
    path (str): La ruta al archivo de imagen.

    Retorna:
    np.ndarray: Los datos de píxeles de la imagen en formato RGB.

    Excepciones:
    ValueError: Si el formato de la imagen no es compatible o si hay un problema al cargar la imagen.
    """
    try:
        # Cargamos la imagen
        image = Image.open(path)
        
        # Aseguramos que la imagen esté en formato RGB (3 colores)
        image = image.convert('RGB')
        
        # Convertimos la imagen a un array de numpy (numerico)
        #el array resultante ser RGB tres dimensiones con los tres 
        # colores o escala de grises dos dimensiones (alto y ancho)
        pixels = np.array(image)
        
        # Imprimimos la forma de la imagen (dimensiones y canales de 
        # color). 
        # {pixels.shape}. Viene de NUmPy usando np.array(image)Es una
        #  tupla de 3 elementos (alto, ancho, canales) en pixeles p.e.
        #  (480,640,3), 480 pix alto 640 pix ancho y 3 colores
        #pixels representa imagen, y .shape nos devuelve una tupla con
        #  las dimensiones del array
        print(f"La forma de la imagen es: {pixels.shape}")
        
        return pixels  # Retornamos los datos de píxeles en formato RGB
    
    except IOError:
        # Si hay un error al cargar la imagen, lanzamos un ValueError
        raise ValueError(f"Error: No se puede cargar la imagen en '{path}'. Por favor, verifica la ruta y el formato del archivo.")
    except Exception as e:
        # Para cualquier otro error inesperado, también lanzamos un ValueError
        raise ValueError(f"Ocurrió un error inesperado: {e}")


