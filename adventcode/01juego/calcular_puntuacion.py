from collections import Counter

def calcular_puntuacion_similitud(archivo):
    # Abrir el archivo y leer las líneas
    with open(archivo, 'r') as file:
        lineas = file.readlines()

    # Separar las dos listas basándonos en las líneas
    lista_izquierda = []
    lista_derecha = []
    
    for linea in lineas:
        num1, num2 = map(int, linea.split())
        lista_izquierda.append(num1)
        lista_derecha.append(num2)

    # Contar la frecuencia de cada número en la lista de la derecha
    frecuencia_derecha = Counter(lista_derecha)
    
    # Calcular la puntuación de similitud
    puntuacion_similitud = 0
    for numero in lista_izquierda:
        puntuacion_similitud += numero * frecuencia_derecha[numero]
    
    return puntuacion_similitud

# Llamar a la función con el archivo input01juego2.txt
archivo = 'input01juego2'
puntuacion = calcular_puntuacion_similitud(archivo)

# Mostrar el resultado
print(f'La puntuación de similitud entre las listas es: {puntuacion}')
