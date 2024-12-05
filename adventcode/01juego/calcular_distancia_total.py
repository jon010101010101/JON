def calcular_distancia_total(archivo):
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
    
    # Ordenar ambas listas
    lista_izquierda.sort()
    lista_derecha.sort()
    
    # Calcular la suma de las distancias
    distancia_total = 0
    for i in range(len(lista_izquierda)):
        distancia_total += abs(lista_izquierda[i] - lista_derecha[i])
    
    return distancia_total

# Llamar a la función con el archivo input01juego.txt
archivo = 'input01juego'
distancia = calcular_distancia_total(archivo)

# Mostrar el resultado
print(f'La distancia total entre las listas es: {distancia}')
