import sys

def get_state_from_capital(capital):
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

    # Crear un diccionario inverso de capital_cities
    cities_to_abbr = {v: k for k, v in capital_cities.items()}
    
    # Crear un diccionario inverso de states
    abbr_to_states = {v: k for k, v in states.items()}

    # Buscar la capital en el diccionario inverso
    if capital in cities_to_abbr:
        # Obtener la abreviatura del estado
        abbr = cities_to_abbr[capital]
        # Obtener el nombre completo del estado
        state = abbr_to_states[abbr]
        print(state)
    else:
        print("Unknown capital city")

if __name__ == '__main__':
    # Verificar si hay exactamente un argumento
    if len(sys.argv) == 2:
        capital = sys.argv[1]
        get_state_from_capital(capital)
    # Si no hay argumentos o hay más de uno, no hacer nada y salir
