import sys

def process_locations(input_string):
    # Define states and capital cities
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

    # Create inverse dictionaries
    state_to_capital = {state: capital_cities[abbr] for state, abbr in states.items()}
    capital_to_state = {capital: state for state, capital in state_to_capital.items()}

    # Process each expression
    expressions = [expr.strip() for expr in input_string.split(',') if expr.strip()]
    
    if not expressions:
        return

    for expr in expressions:
        expr = expr.title()
        
        if expr in state_to_capital:
            print(f"{state_to_capital[expr]} is the capital of {expr}")
        elif expr in capital_to_state:
            print(f"{expr} is the capital of {capital_to_state[expr]}")
        else:
            print(f"{expr} is neither a capital city nor a state")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        process_locations(sys.argv[1])







#py all_in.py "New jersey, Tren ton, NewJersey, Trenton, toto, , sAlem"
 