def read_numbers():
	[print(str_digit.strip()) for str_digit in open('numbers.txt', 'r').read().split(',')]

if __name__ == "__main__":
	read_numbers()
