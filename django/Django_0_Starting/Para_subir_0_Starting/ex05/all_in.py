import sys

def process_locations(input_string):
    # Define the states and capital cities dictionaries
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

    # Create inverse dictionaries for easier lookup
    state_to_capital = {state: capital_cities[abbr] for state, abbr in states.items()}
    capital_to_state = {capital: state for state, capital in state_to_capital.items()}

    # Process each expression in the input string
    expressions = [expr.strip() for expr in input_string.split(',')]
    
    # Check for consecutive commas (empty expressions)
    if '' in expressions:
        return  # Exit if there are consecutive commas

    for expr in expressions:
        # Convert to title case to standardize input
        expr = expr.title()
        
        # Check if the expression is a state
        if expr in state_to_capital:
            print(f"{state_to_capital[expr]} is the capital of {expr}")
        # Check if the expression is a capital city
        elif expr in capital_to_state:
            print(f"{expr} is the capital of {capital_to_state[expr]}")
        # If it's neither a state nor a capital city
        else:
            print(f"{expr} is neither a capital city nor a state")

if __name__ == '__main__':
    # Check if there is exactly one command-line argument
    if len(sys.argv) == 2:
        process_locations(sys.argv[1])



#py all_in.py "New jersey, Tren ton, NewJersey, Trenton, toto, Salem"
 