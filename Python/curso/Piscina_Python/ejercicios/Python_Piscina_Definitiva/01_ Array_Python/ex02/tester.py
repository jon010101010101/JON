from load_image import ft_load  # Importamos la función desde array2D

if __name__ == "__main__":  # Comprobamos si este archivo se está ejecutando directamente
    try:
        # Llamamos a la función ft_load y almacenamos los píxeles en la variable
        pixels = ft_load("landscape.jpg")
        print(pixels)  # Imprimimos el contenido de los píxeles
    except ValueError as e:
        # Si ocurre un ValueError, lo imprimimos
        print(e)
