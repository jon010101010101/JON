from typing import Any, List, Union # typing es para importaciones de tipos
# de datos esperados en funciones y variables.
# Any, puede ser variable de cualquier tipo, list, se usa para anotar listas, 
# Union, para indicar que una variable puede ser de varios tipos especifficados
from math import sqrt #math modulo matemaricas, sqrt (raiz cuaddrada)

# Función para calcular la media de una lista de números
def mean(ls: List[Union[int, float]]) -> float:
    """Calculates the mean of a list."""
    return sum(ls) / len(ls)

# Función para calcular la mediana de una lista de números
def median(ls: List[Union[int, float]]) -> float: # ls indica lista de float o int devuleve float
    """Calculates the median of a list."""
    sorted_ls = sorted(ls) # crea lista con los numeros ordenados de menor a mayor
    mid = len(sorted_ls) // 2 #calcula el indice medio y redondea hacia abajo. // division
    # Si la longitud de la lista es impar, devuelve el elemento del medio
    if len(sorted_ls) % 2 != 0: # si el operador devuleve resto es impar
        return sorted_ls[mid] #devuleve la posicion media
    # Si es par, devuelve el promedio de los dos elementos del medio
    else:
        return (sorted_ls[mid - 1] + sorted_ls[mid]) / 2
        # sorted_ls[mid - 1] es el elemento justo antes del medio. y sorted_ls[mid]
        # es el elemento justo después del medio. Se suman y div ente 2 para sacar promedio

# Función para calcular los cuartiles (25% y 75%) de una lista de números
def quartile(ls: List[Union[int, float]]) -> List[float]:
    """Calculate Quartile (25% and 75%)"""
    # Caso especial: si la lista tiene un solo elemento, en este caso los quartiles
    #  son iguales
    if len(ls) == 1:
        return [ls[0], ls[0]]
    
    s = sorted(ls) #ordenamos de menor a mayor
    mid = int(len(s) / 2) # calculamos el indice medio de la lista
    # Ajuste para listas de longitud impar
    m1 = mid + 1 if len(s) % 2 else mid # Si la longitud es impar, m1 será mid + 1,
    # si es par, será igual a mid, esto asegura que la primera mitad incluya el 
    # elemento medio en listas impares
    # Calcula el primer y tercer cuartil
    # Calculamos el primer y tercer cuartil
    # El primer cuartil (Q1) es la mediana de la primera mitad de la lista
    # El tercer cuartil (Q3) es la mediana de la segunda mitad de la lista
    # Usamos la función median() (que debe estar definida en otra parte del código)
    return [float(median(s[:m1])), float(median(s[mid:]))]

# Función para calcular la varianza de una lista de números
def var(ls: List[Union[int, float]]) -> float:
    """Calculates the variance of a list."""
    m = mean(ls) #calculamos la media de la lista
    # Suma de los cuadrados de las diferencias con la media
    return sum([(x - m) ** 2 for x in ls]) / len(ls)
    # Calculamos la varianza:
    # 1. Restamos la media a cada elemento de la lista
    # 2. Elevamos al cuadrado cada diferencia
    # 3. Sumamos todos estos cuadrados
    # 4. Dividimos por el número total de elementos

# Función para calcular la desviación estándar de una lista de números
def std(ls: List[Union[int, float]]) -> float:
    """Calculates the standard deviation of a list."""
    return sqrt(var(ls))
    # Calculamos la desviación estándar:
    # 1. Primero calculamos la varianza usando la función var()
    # 2. Luego calculamos la raíz cuadrada de la varianza

# Función principal para calcular estadísticas
def ft_statistics(*args: Union[int, float], **kwargs: dict) -> None:
    """
    Calculates various statistical measures based on the provided
    numerical arguments.
    """

    # Filtrar números válidos de args
    # Creamos una lista con solo los argumentos que son enteros o flotantes
    nums = [x for x in args if isinstance(x, (int, float))]
    # es una lista de comprensión para flitrar los argumentos numericos validos
    # args. Es una tupla que contiene todos los argumentos posicionales pasados 
    # a la función.
    # for x in args. Itera sobre cada elemento x en args
    # primer x, es el valor que se incluira en la ueva lista si cumple la condición,
    #  y queremos meterlo exactamente igual que esta sin modificarlo

    # Definir operaciones válidas
     # Conjunto de operaciones estadísticas que la función puede realizar
    valid_operations = {"mean", "median", "quartile", "std", "var"}

    # Comprobar si hay números válidos
    if not nums:
        # Si no hay números válidos, imprimir "ERROR" por cada operación solicitada
        for value in kwargs.values(): # bucle que itera cada kwargs que tiene los 
            # argumentos pasados con nombre de funcion del diccionario
            print("ERROR")
        return

    # Procesar cada operación solicitada en kwargs
    for value in kwargs.values():
        if value not in valid_operations: # comprueba si valor actual es uno de kwargs
            # previamente definios (valid_operations)
            continue  # No hacer nada si la operación no es válida, salta el bucle.
                    #  Permite a la función ignorar silenciosamente cualquier 
                    # operación solicitada que no sea válida, en lugar de dar error.
        else: # se ejecuta si la ccondicion anterior (if) es falsa
            # Ejecutar la operación correspondiente e imprimir el resultado
            if value == "mean":
                print(f"mean : {mean(nums)}")
            elif value == "median":
                print(f"median : {median(nums)}")
            elif value == "quartile":
                print(f"quartile : {quartile(nums)}")
            elif value == "var":
                print(f"var : {var(nums)}")
            elif value == "std":
                print(f"std : {std(nums)}")
            # se va comprobando si cada operacion coincide con el kwards, si es asi
            # se ejecuta y se imprime formateado, para incluir el resultado de la
            # función directamente en la cadena de texto