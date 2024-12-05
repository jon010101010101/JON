import numpy as np
import matplotlib.pyplot as plt  # Importar para visualización


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Invierte los colores de la imagen recibida.

    Args:
        array (np.ndarray): El arreglo de la imagen de entrada.

    Returns:
        np.ndarray: El arreglo de la imagen invertida.
    """
    # Inversión de colores. Convierte los pixeles negro (0) en blancos
    #  (255) y al reves
    inverted = 255 - array
    display_image(inverted, "Inverted Image") #mostrar imagen
    return inverted


def ft_red(array: np.ndarray) -> np.ndarray:
    """Mantiene el canal rojo de la imagen, estableciendo los demás en cero.

    Args:
        array (np.ndarray): El arreglo de la imagen de entrada.

    Returns:
        np.ndarray: El arreglo de la imagen filtrada en rojo.
    """
    red_array = np.copy(array)  # Crear una copia para evitar modificar el original
    red_array[:, :, 1] = 0  # Establecer el canal verde en 0
    red_array[:, :, 2] = 0  # Establecer el canal azul en 0
    display_image(red_array, "Imagen Filtrada en Rojo")
    return red_array


def ft_green(array: np.ndarray) -> np.ndarray:
    """Mantiene el canal verde de la imagen, estableciendo los demás en cero.

    Args:
        array (np.ndarray): El arreglo de la imagen de entrada.

    Returns:
        np.ndarray: El arreglo de la imagen filtrada en verde.
    """
    # Crear una copia para evitar modificar el original
    green_array = np.copy(array)
    green_array[:, :, 0] = 0  # Establecer el canal rojo en 0
    green_array[:, :, 2] = 0  # Establecer el canal azul en 0
    display_image(green_array, "Imagen Filtrada en Verde")
    return green_array


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Mantiene el canal azul de la imagen, estableciendo los demás en cero.

    Args:
        array (np.ndarray): El arreglo de la imagen de entrada.

    Returns:
        np.ndarray: El arreglo de la imagen filtrada en azul.
    """
    # Crear una copia para evitar modificar el original
    blue_array = np.copy(array)
    blue_array[:, :, 0] = 0  # Establecer el canal rojo en 0
    blue_array[:, :, 1] = 0  # Establecer el canal verde en 0
    display_image(blue_array, "Imagen Filtrada en Azul")
    return blue_array


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Convierte la imagen a escala de grises promediando los colores básicos.

    Args:
        array (np.ndarray): El arreglo de la imagen de entrada.

    Returns:
        np.ndarray: El arreglo de la imagen en escala de grises.
    """
    # Calcular promedio del eje 2 axis=2. .astype(np.uint8) 
    # invierte cclores blanco a negro
    grey_array = np.mean(array, axis=2).astype(np.uint8)
    # (grey_array,) * 3 crea un a tupla de 3 copias, np.stack la apila.
    # axis=-1 especifica que el nuevo eje debe ser el ultimo (eje canales
    # de color) RGB
    grey_image = np.stack((grey_array,) * 3, axis=-1)

    display_image(grey_image, "Imagen en Escala de Grises")

    return grey_image


def display_image(imagen, titulo):
    """Muestra una sola imagen en un gráfico.

    Args:
        imagen (np.ndarray): La imagen a mostrar.
        titulo (str): El título del gráfico.
    """
    plt.imshow(imagen) # muestra imagen actual
    plt.title(titulo) #añade el titulo
    plt.axis('off') # elimina los bordes y marccas de los ejes alrededor 
    #de la imagen
    plt.show()  # Mostrar la imagen filtrada
