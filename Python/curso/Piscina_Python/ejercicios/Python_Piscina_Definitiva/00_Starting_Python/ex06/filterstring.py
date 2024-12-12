"""
Filtra palabras de una cadena basándose en su longitud.

Uso: python3 filterstring.py 'cadena de texto' longitud_mínima

Ejemplo: python3 filterstring.py 'Hello the World' 3
"""

import sys

def ft_filter(func, iterable):
    """
    Filtra los elementos del iterable según la función proporcionada.
    
    Args:
        func: Función que determina si un elemento debe ser incluido.
        iterable: Iterable a filtrar.

    Returns:
        List de elementos que cumplen la condición.
    """
    return [item for item in iterable if func(item)]

def main():
    """
    Función principal que procesa los argumentos de la línea de comandos,
    filtra las palabras y muestra el resultado.

    Raises:
        AssertionError: Si los argumentos proporcionados son incorrectos.
    """
    # Verificar que se proporcionen exactamente dos argumentos
    if len(sys.argv) != 3:
        raise AssertionError("AssertionError: the arguments are bad")

    # Asignar el primer argumento (la cadena) a la variable sentence
    sentence = sys.argv[1]

    try:
        # Convertir el segundo argumento a entero y asignarlo a length
        length = int(sys.argv[2])
    except ValueError:
        raise AssertionError("AssertionError: the arguments are bad")

    # Dividir la cadena en palabras
    words = sentence.split()

    # Filtrar las palabras usando ft_filter y una expresión lambda
    filtered_words = ft_filter(lambda word: len(word) >= length, words)

    print(filtered_words)  # Imprimir la lista de palabras filtradas

if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(e)  # Imprimir solo el mensaje de error sin el traceback

"""
¿Qué es una función lambda?
Las funciones lambda en Python son funciones anónimas, es decir, funciones sin
 nombre que se definen utilizando la palabra clave lambda. Son útiles para crear
funciones pequeñas y rápidas en una sola línea de código, especialmente cuando 
se utilizan como argumentos para otras funciones de orden superior como filter(),
map(), y reduce().

lambda argumentos: expresión

Solo pueden contener una expresión (no múltiples sentencias)
No se pueden usar para definir funciones complejas que requieran múltiples líneas
 de código.

"""

"""

"""