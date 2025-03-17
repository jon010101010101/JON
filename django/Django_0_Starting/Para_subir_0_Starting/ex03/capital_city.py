import sys

def get_capital_city(state):
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

    # Check if the state is in the states dictionary
    if state in states:
        # Get the state abbreviation
        abbreviation = states[state]
        # Get the capital city using the abbreviation
        capital = capital_cities[abbreviation]
        print(capital)
    else:
        print("Unknown state")

if __name__ == '__main__':
    # Check if there's exactly one argument (excluding the script name)
    if len(sys.argv) == 2:
        state = sys.argv[1]
        get_capital_city(state)
    # If there are no arguments or more than one, do nothing and quit
