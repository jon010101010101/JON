import numpy as np  # Importar numpy para trabajar con arrays
import matplotlib.pyplot as plt  # Importar matplotlib para la visualización de imágenes
from PIL import Image  # Importar la biblioteca PIL para la manipulación de imágenes
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
        # Convertir la imagen a un array de numpy
        pixels = np.array(image)
        return pixels  # Retornar los datos de píxeles en formato RGB

    except IOError:
        raise ValueError(
            f"Error: No se puede cargar la imagen en '{path}'. "
            "Por favor, verifica la ruta y el formato del archivo."
        )
    except Exception as e:
        raise ValueError(f"Ocurrió un error inesperado: {e}")

def convert_to_grayscale(image: np.ndarray) -> np.ndarray:
    """
    Convierte una imagen RGB a escala de grises utilizando el método de luminosidad.

    Parámetros:
    image (np.ndarray): La imagen RGB a convertir.

    Retorna:
    np.ndarray: Imagen en escala de grises.
    """
    # Usar el producto punto para convertir a escala de grises
    # .... significa todas las dimensiones anteriores
    # 3 selecccion los tres ultimos elementos del array anterior, tipica 
    # de un formato RGB, Array es convinacion para escala de grises
    grayscale_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
    
    # Retornar como uint8, numero enterro sin signo de 8 bits, por que 
    # la mayoria de formatos imagen JPEG, ONG utilizan 8 bits
    return grayscale_image.astype(np.uint8)  

# Cargar la imagen usando la función definida
image = ft_load('animal.jpeg')

# Mostrar la forma original de la imagen en consola
print(f"La forma de la imagen es: {image.shape}")

# Cortar un cuadrado de 400x400 desde el centro de la imagen
height, width, _ = image.shape  # Obtener las dimensiones de la imagen
start_height = (height - 400) // 2  # Calcular el punto de inicio en altura
start_width = (width - 400) // 2  # Calcular el punto de inicio en anchura
cropped_image = image[start_height:start_height + 400, start_width:start_width + 400]  # Recortar

# Transponer la imagen recortada (intercambiar filas y columnas), 
# Si cropped_image tiene forma (100, 200, 3), transposed_image tendrá 
# forma (200, 100, 3). Asi rota la foto

transposed_image = cropped_image.transpose(1, 0, 2)

# Convertir la imagen transpuesta a escala de grises
grayscale_transposed_image = convert_to_grayscale(transposed_image)

# Mostrar la nueva forma de la imagen transpuesta en consola
print(f"Nueva forma después de transponer: {grayscale_transposed_image.shape}")

# Mostrar los datos de píxeles de la imagen transpuesta (imprimir todos los valores)
print(grayscale_transposed_image)

# Mostrar la imagen transpuesta usando matplotlib
# Usar cmap='gray' que asegura que salga escala de grisis si no mezcla pero no
#  bien
plt.imshow(grayscale_transposed_image, cmap='gray')
plt.axis('on')  # Activar ejes para ver las leyendas

# Configurar las leyendas de los ejes cada 50 píxeles
# Leyendas del eje x (altura por esta rotate) cada 50 píxeles. 1 es segundo elemento
# shape (indice =) es altura original e indice 1 anchura, al rotal son al reves, para 
# que mantengan las medidas originales
plt.xticks(ticks=np.arange(0, grayscale_transposed_image.shape[1], 50))
# Leyendas del eje y (ancho por estar rotate)cada 50 píxeles
plt.yticks(ticks=np.arange(0, grayscale_transposed_image.shape[0], 50))

plt.show()  # Mostrar la ventana con la imagen transpuesta en escala de grises


