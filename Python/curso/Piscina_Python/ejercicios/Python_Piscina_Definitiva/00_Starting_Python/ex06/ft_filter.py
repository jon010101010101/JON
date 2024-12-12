def ft_filter(func, iterable):
    """
    Filtra los elementos del iterable según la función proporcionada.
    
    Args:
        func: Función que determina si un elemento debe ser incluido.
        iterable: Iterable a filtrar.

    Returns:
        List de elementos que cumplen la condición.
    """
    return [item for item in iterable if func(item)] #lista de compresion

"""
¿Qué es una lista de comprensión?
Una lista de comprensión es una forma concisa y eficiente de crear listas en
 Python. Permite generar una nueva lista aplicando una expresión a cada 
 elemento de un iterable (como una lista o un rango) y, opcionalmente, 
 filtrando elementos con una condición.
Sintaxis
La sintaxis básica de una lista de comprensión es:

nueva_lista = [expresión for elemento in iterable if condición]

Ventajas de las Listas de Comprensión

    Concisión: Permiten escribir menos código para lograr el mismo resultado.
    Legibilidad: A menudo son más fáciles de leer y entender que los bucles 
    tradicionales.
    Eficiencia: Son generalmente más rápidas que usar un bucle for convencional
     para construir listas.


<list> es el tipo de datos, mientras que la lista de comprensión es una técnica
 para crear listas.
 """