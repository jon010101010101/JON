import sys

def guess_capital(capital):
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

	for state in states:
		if capital_cities[states[state]] == capital:
			return state
	else:
		sys.exit('Unknown capital city')

if __name__ == "__main__":
	if len(sys.argv) != 2:
		exit
	else:
		print(guess_capital(sys.argv[1]))
