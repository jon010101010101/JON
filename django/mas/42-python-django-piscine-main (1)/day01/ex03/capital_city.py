import sys

def guess_capital(state):
	states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
	}
	capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
	}
	if state in states:
		print(capital_cities[states[state]])
	else:
		print("Unknown state")

if __name__ == "__main__":
	if len(sys.argv) != 2:
		exit
	else:
		guess_capital(sys.argv[1])
