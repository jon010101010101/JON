import sys
import antigravity

def geohashing():
	try:
		antigravity.geohash(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3].encode('UTF-8'))
	except Exception as error:
		print(error)


if __name__ == "__main__":
	if len(sys.argv) != 5:
		sys.exit('Wrong number of parameters; try latitude, longitude, date, indice_dow')
	else:
		geohashing()
