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
        
        # Aseguramos que la imagen esté en formato RGB
        image = image.convert('RGB')
        
        # Convertimos la imagen a un array de numpy
        pixels = np.array(image)
        
        # Imprimimos la forma de la imagen (dimensiones y canales de color)
        print(f"La forma de la imagen es: {pixels.shape}")
        
        return pixels  # Retornamos los datos de píxeles en formato RGB
    
    except IOError:
        # Si hay un error al cargar la imagen, lanzamos un ValueError
        raise ValueError(f"Error: No se puede cargar la imagen en '{path}'. Por favor, verifica la ruta y el formato del archivo.")
    except Exception as e:
        # Para cualquier otro error inesperado, también lanzamos un ValueError
        raise ValueError(f"Ocurrió un error inesperado: {e}")

def save_image(pixels: np.ndarray, path: str):
    """
    Guarda los datos de píxeles en un archivo de imagen.

    Parámetros:
    pixels (np.ndarray): Los datos de píxeles en formato RGB.
    path (str): La ruta donde se guardará la imagen.
    """
    try:
        # Convertimos el array de píxeles de vuelta a una imagen
        image = Image.fromarray(pixels.astype('uint8'), 'RGB')
        image.save(path)  # Guardamos la imagen
        print(f"Imagen guardada como '{path}'")  # Mensaje de éxito
    except Exception as e:
        raise ValueError(f"Error al guardar la imagen: {e}")

if __name__ == "__main__":  # Comprobamos si este archivo se está ejecutando directamente
    try:
        # Llamamos a la función ft_load y almacenamos los píxeles en la variable
        pixels = ft_load("landscape.jpg")  # Asegúrate de que la imagen esté en el mismo directorio
        print(pixels)  # Imprimimos el contenido de los píxeles

        # Guardamos la imagen resultante en un nuevo archivo
        save_image(pixels, "output_image.png")  # Cambia el nombre de archivo según sea necesario
    except ValueError as e:
        # Si ocurre un ValueError, lo imprimimos
        print(e)
