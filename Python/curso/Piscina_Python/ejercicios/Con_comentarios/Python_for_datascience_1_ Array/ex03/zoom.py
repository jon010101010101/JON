
from PIL import Image  # Importar la biblioteca PIL para la manipulación de imágenes
import numpy as np  # Importar numpy para trabajar con arreglos
import matplotlib.pyplot as plt  # Importar matplotlib para la visualización de imágenes
from load_image import ft_load  # Importar la función de carga desde el archivo load_image.py

def apply_zoom(image: np.ndarray) -> np.ndarray:
    """
    Aplica zoom a la imagen recortando su contenido.

    Parámetros:
    image (np.ndarray): La imagen a la que se aplicará el zoom.

    Retorna:
    np.ndarray: Imagen recortada.
    """
    height, width, _ = image.shape  # Obtener las dimensiones de la imagen

    # Ajustar el punto de inicio para el recorte para centrar la cara
    start_height = 100  # Ajustar según la posición vertical de la cara
    start_width = 448   # Ajustar según la posición horizontal de la cara

    # Especificar el tamaño del recorte
    new_height = 400
    new_width = 400

    # Asegurarse de que el recorte no salga de los límites. 
    # Si es negativo se establece el = si es positivo se mantiene su valor
    start_height = max(0, start_height)
    start_width = max(0, start_width)

    # Recortar la imagen al nuevo tamaño. Se conoce como slicing.
    # Si el array es a:b el sciling va dde a a b-1
    # Crea un nuevo array que es una subregión del array original
    # selciona filas/columnas de star_heigt hasta start_height + 
    # new_height - 1
    zoomed_image = image[
        start_height:start_height + new_height,
        start_width:start_width + new_width
    ]

    return zoomed_image  # Retornar la imagen recortada en color

def convert_to_grayscale(image: np.ndarray) -> np.ndarray:
    """
    Converts an RGB image to grayscale.

    Parameters:
    image (np.ndarray): The RGB image to convert.

    Returns:
    np.ndarray: Grayscale image.
    """
    # # Convert using luminosity method
    # ... mantiene las dimensiones anteriores sin cambos
    # 3 selecciona los primeros 3 canales generalmete RGB
    # np.dot multiplica cada canal de color por su coeficiente y suma resultado
    grayscale_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])

    # Return as uint8, rtorno a entero sin signo de 8 bits, optimiza 
    # memoria y es eficiente para operaciones aritmeticas basicas y 
    # comparaciones
    return grayscale_image.astype(np.uint8)

# Cargar una imagen usando la función de carga
image_path = 'animal.jpeg' # ruta a la imagen
image_np = ft_load(image_path)  # Cargar la imagen y obtener los datos 
# de píxeles. Trae la imagen desde image_path (ruta hasta imagen), 
# convierte a RGB y crea un array de la imagen

# Aplicar zoom a la imagen
zoomed_image = apply_zoom(image_np)  # Llamar a la función para aplicar el zoom

# Imprimir la nueva forma de la imagen recortada
print("Nueva forma después del recorte:", zoomed_image.shape)

# Mostrar la imagen recortada usando matplotlib
plt.imshow(zoomed_image)  # Mostrar la imagen recortada
plt.axis('on')  # Mostrar los ejes para ver la escala
#plt.title('Imagen con Zoom')  # Título de la ventana de visualización
plt.show()  # Mostrar la ventana con la imagen

