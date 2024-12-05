def leer_datos_archivo(ruta_archivo):
    # Leer el archivo y convertirlo en una lista de listas de caracteres
    matriz = []
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            matriz.append(list(linea.strip()))  # Eliminar saltos de línea y convertir en lista
    return matriz

def buscar_XMAS(matriz):
    # Contador para las instancias de X-MAS
    count = 0
    rows = len(matriz)
    cols = len(matriz[0])

    # Función para verificar el patrón en una dirección específica
    def verificar_XMAS(i, j, dx, dy):
        # Verificar que los índices no salgan de la matriz
        if (0 <= i + 2*dx < rows and 0 <= j + 2*dy < cols and
            0 <= i - dx < rows and 0 <= j - dy < cols and
            0 <= i - 2*dx < rows and 0 <= j - 2*dy < cols):  # Verificación adicional
            # Verificar si las letras corresponden al patrón "M", "S", "M", "S", "A"
            if (matriz[i][j] == 'M' and
                matriz[i + dx][j + dy] == 'S' and
                matriz[i + 2*dx][j + 2*dy] == 'M' and
                matriz[i - dx][j - dy] == 'S' and
                matriz[i - 2*dx][j - 2*dy] == 'A'):
                return True
        return False

    # Recorrer la matriz y verificar las 8 direcciones posibles para encontrar el patrón
    for i in range(rows):
        for j in range(cols):
            # Verificar todas las direcciones posibles
            if verificar_XMAS(i, j, 1, 1):  # Descendente diagonal hacia abajo y a la derecha
                count += 1
            if verificar_XMAS(i, j, 1, -1):  # Ascendente diagonal hacia abajo y a la izquierda
                count += 1
            if verificar_XMAS(i, j, -1, 1):  # Descendente diagonal hacia arriba y a la derecha
                count += 1
            if verificar_XMAS(i, j, -1, -1):  # Ascendente diagonal hacia arriba y a la izquierda
                count += 1
            
            # Verificar también en direcciones horizontales y verticales
            if verificar_XMAS(i, j, 0, 1):  # Horizontal hacia la derecha
                count += 1
            if verificar_XMAS(i, j, 0, -1):  # Horizontal hacia la izquierda
                count += 1
            if verificar_XMAS(i, j, 1, 0):  # Vertical hacia abajo
                count += 1
            if verificar_XMAS(i, j, -1, 0):  # Vertical hacia arriba
                count += 1

    return count

# Ruta al archivo de entrada
ruta_archivo = 'input04juego2'  # Asegúrate de que el archivo está en el mismo directorio

# Leer los datos del archivo
matriz = leer_datos_archivo(ruta_archivo)

# Llamamos a la función para contar cuántas veces aparece el patrón "X-MAS"
resultado = buscar_XMAS(matriz)
print("Número de veces que aparece el patrón X-MAS:", resultado)
