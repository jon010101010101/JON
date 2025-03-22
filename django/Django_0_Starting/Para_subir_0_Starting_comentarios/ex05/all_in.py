import sys  # Importar el módulo sys para trabajar con argumentos de línea de comandos.

def process_locations(input_string):
    # Definir los diccionarios de estados y ciudades capitales.
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    # Crear diccionarios inversos para facilitar la búsqueda:
    # `state_to_capital` mapea estados a sus respectivas capitales.
    state_to_capital = {state: capital_cities[abbr] for state, abbr in states.items()}
    # `capital_to_state` mapea ciudades capitales a sus respectivos estados.
    capital_to_state = {capital: state for state, capital in state_to_capital.items()}

    # Dividir la cadena de entrada en expresiones separadas por comas y eliminar espacios adicionales.
    expressions = [expr.strip() for expr in input_string.split(',')]
    
    # Verificar si hay comas consecutivas (lo que generaría expresiones vacías).
    if '' in expressions:
        return  # Salir de la función si hay expresiones vacías.

    # Para manejar el espacio vacio entre dos comas
    expressions = [expr.strip() for expr in input_string.split(',') if expr.strip()]

    # Iterar sobre cada expresión procesada.
    for expr in expressions:
        # Convertir la expresión a formato de título (primera letra mayúscula) para estandarizar la entrada.
        expr = expr.title()
        
        # Verificar si la expresión es un estado.
        if expr in state_to_capital:
            print(f"{state_to_capital[expr]} is the capital of {expr}")
        # Verificar si la expresión es una ciudad capital.
        elif expr in capital_to_state:
            print(f"{expr} is the capital of {capital_to_state[expr]}")
        # Si no es ni un estado ni una ciudad capital.
        else:
            print(f"{expr} is neither a capital city nor a state")

# Punto de entrada principal del script.
if __name__ == '__main__':
    # Verificar si se pasa exactamente un argumento al script (además del nombre del script).
    if len(sys.argv) == 2:
        process_locations(sys.argv[1])  # Llamar a la función con el argumento proporcionado.




# py all_in.py "New jersey, Tren ton, NewJersey, Trenton, toto,      sAlem"
