import sys  # Import the sys module to access command-line arguments.

def get_capital_city(state):
    # Dictionary mapping state names to their abbreviations.
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    # Dictionary mapping state abbreviations to their capital cities.
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    # Check if the provided state is in the `states` dictionary.
    if state in states:
        abbreviation = states[state]
        capital = capital_cities[abbreviation]
        print(capital)
    else:
        print("Unknown state")


if __name__ == '__main__':
    # Check if there's exactly one argument (excluding the script name).
    if len(sys.argv) == 2:
        state = sys.argv[1]
        get_capital_city(state)


