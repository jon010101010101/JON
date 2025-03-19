import sys  # Importar el módulo sys para acceder a los argumentos de la línea de comandos.

def get_capital_city(state):
    # Diccionario que mapea los nombres de los estados a sus abreviaturas.
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    # Diccionario que mapea las abreviaturas de los estados a sus capitales.
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    # Verificar si el estado proporcionado está en el diccionario `states`.
    if state in states:
        # Obtener la abreviatura del estado.
        abbreviation = states[state]
        # Usar la abreviatura para obtener la ciudad capital del diccionario `capital_cities`.
        capital = capital_cities[abbreviation]
        print(capital)  # Imprimir la ciudad capital.
    else:
        # Si el estado no está en el diccionario, imprimir un mensaje indicando que es desconocido.
        print("Unknown state")

# Punto de entrada principal del script.
if __name__ == '__main__':
    # Verificar si hay exactamente un argumento (excluyendo el nombre del script).
    if len(sys.argv) == 2: # Asegura que hay solo un argumento, indice 0 y argumento (indice 1)
        state = sys.argv[1]  # Obtener el argumento proporcionado desde la línea de comandos.
        get_capital_city(state)  # Llamar a la función con el estado proporcionado.
    # Si no hay argumentos o hay más de uno, no hacer nada y salir del programa.

