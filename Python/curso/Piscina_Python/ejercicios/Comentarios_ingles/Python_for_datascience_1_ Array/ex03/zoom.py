import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load
import os
import sys
import warnings


def cut_square(image: np.ndarray,
               start_height: int,
               start_width: int,
               size: int = 400) -> np.ndarray:
    height, width, _ = image.shape
    if start_height + size > height or start_width + size > width:
        raise ValueError("Error: The cut exceeds the image boundaries.")
    return image[start_height:start_height + size,
                 start_width:start_width + size]


def to_grayscale(image: np.ndarray) -> np.ndarray:
    return np.dot(image[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)


def main():
    warnings.filterwarnings("ignore")
    original_stderr = sys.stderr
    sys.stderr = open(os.devnull, 'w')

    try:
        image_path = 'animal.jpeg'

        if not os.path.exists(image_path):
            print(f"Error: The file '{image_path}' does not exist.")
            return

        _, ext = os.path.splitext(image_path)
        if ext.lower() not in ['.jpg', '.jpeg']:
            print("Error: The file must be in JPG or JPEG format.")
            return

        image = ft_load(image_path)
        print(f"The shape of image is: {image.shape}")
        #svciling de 3 x 3
        print(image[:3, :3])

        start_height = 100
        start_width = 450

        #llama a la funcion cut_square para recortar lo señalado 
        # imagen, donde empezara con coordinada y y coordinada x
        square_image = cut_square(image, start_height, start_width)
        # la imagen recortada a escala de grises
        gray_image = to_grayscale(square_image)
        # le cambia lass dimensiones para (400x400) a (400x400x1), como
        #normalmente la escala de grises se representa en array2D, le pone 1
        # un unico canal, asi tiene 3 canales para RGB
        gray_image = gray_image.reshape(400, 400, 1)
        #coge la imagen ·D y solo coge los dos primeros 400x400
        print(f"New shape after slicing: {gray_image.shape} "
              f"or {gray_image.shape[:2]}")
        #pasamos de 400, 400 a 400,400,1 y luego vuelta a 400 ,400, esto se hace
        # consistencia en los datos, muchas bibliotecas piden que sea tridimensional
        # y luego es facil si se necesta pasar a dos canales

        print(gray_image[:3, :3])

        # Set ticks and labels for axes from 0 to 350 in increments of 50
        ticks = np.arange(0, 351, 50)
        
        plt.figure(figsize=(4, 4))
        #squeeze convierte 400x400x1 por 400x400.
        # cmap='gray paleta de grisis para visualizar
        plt.imshow(gray_image.squeeze(), cmap='gray')
        
        # Set limits for the axes
        plt.xlim(0, 400)
        plt.ylim(400, 0)  # Estable los limites de x e y
        #coloca las marcas de los ejeses usando los valores ticks
        plt.xticks(ticks)
        plt.yticks(ticks)
        
        plt.axis('on') #hace que sean visibles
        plt.show()

    #captura cualquier error no manejado anterioirmente e indica la clase
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

    #se ejecuta independientemente de si ha habido error o no
    finally:
        #Cierra el flujo de error estándar que fue redirigido anteriormente.
        sys.stderr.close()
        #Restaura el flujo de error estándar original, para que se muestren 
        # futuros errores
        sys.stderr = original_stderr


#Comprueba si el script está siendo ejecutado directamente (no importado como módulo).
if __name__ == "__main__":
    main()
# Si el script se está ejecutando directamente, llama a la función main()