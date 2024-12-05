# tester de varias pruebas #

from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

if __name__ == "__main__":
    # Prueba con rango pequeño
    print("Usando ft_tqdm con rango pequeño:")
    for elem in ft_tqdm(range(5)):  # Itera sobre un rango pequeño
        sleep(0.5)  # Simula tiempo de trabajo
   
    print("Usando tqdm con rango pequeño:")
    for elem in tqdm(range(5)):  
        sleep(0.5)  # Simula tiempo de trabajo
    print()  # Nueva línea al finalizar

    # Prueba con rango grande
    print("Usando ft_tqdm con rango grande:")
    for elem in ft_tqdm(range(1000)):  
        sleep(0.001)  
    
    print("Usando tqdm con rango grande:")
    for elem in tqdm(range(1000)): 
        sleep(0.001)  
    print()  # Nueva línea al finalizar

    # Prueba con rango vacío
    print("Usando ft_tqdm con rango vacío:")
    for elem in ft_tqdm(range(0)):  # Esto debería indicar que está vacío
        sleep(0.5)  # No se procesará ningún elemento
    
    print("Usando tqdm con rango vacío:")
    for elem in tqdm(range(0)):  # Esto debería indicar que está vacío
        sleep(0.5)  # No se procesará ningún elemento
    print()  

    # Prueba con rango de un solo elemento
    print("Usando ft_tqdm con rango de un solo elemento:")
    for elem in ft_tqdm(range(1)):  
        sleep(0.5)  
    
    print("Usando tqdm con rango de un solo elemento:")
    for elem in tqdm(range(1)):
        sleep(0.5)  
    print()

    # Prueba con argumento no válido
    print("Usando ft_tqdm con argumento no válido:")
    try:
        for elem in ft_tqdm("string"):  # Esto debería fallar porque "string" no es un rango
            sleep(0.5)  
    except TypeError as e:
        print("Error: El argumento debe ser de tipo range.")  # Mensaje de error 

    print("Usando tqdm con argumento no válido:")
    try:
        # Verificar si el argumento es una cadena y lanzar un error manualmente
        if isinstance("string", str):
            raise TypeError("El argumento debe ser de tipo range.")
        for elem in tqdm("string"):  # Esto también debería fallar
            sleep(0.5) 
    except TypeError as e:
        print("Error: El argumento debe ser de tipo range.")  # Mensaje de error 
