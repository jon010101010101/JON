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

    # Create an inverse dictionary of capital_cities
    cities_to_abbr = {v: k for k, v in capital_cities.items()}
    
    # Create an inverse dictionary of states
    abbr_to_states = {v: k for k, v in states.items()}

    # Look up the capital in the inverse dictionary
    if capital in cities_to_abbr:
        abbr = cities_to_abbr[capital]
        state = abbr_to_states[abbr]
        print(state)
    else:
        print("Unknown capital city")

if __name__ == '__main__':
    # Check if there is exactly one argument
    if len(sys.argv) == 2:
        capital = sys.argv[1]
        get_state_from_capital(capital)


