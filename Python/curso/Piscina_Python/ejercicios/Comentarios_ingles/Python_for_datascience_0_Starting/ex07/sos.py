import sys

# Dictionary that contains the representations in Morse code
NESTED_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'  # The space is represented as a /
}


def encode_to_morse(input_string):
    """Encodes the input string to Morse code."""
    morse_code = []  # List to store the Morse code
    for char in input_string.upper():  # Convert to uppercase for consistency
        if char in NESTED_MORSE:  # Check if the character is in the dictionary
            morse_code.append(NESTED_MORSE[char])  # Append the corresponding
            # Morse code
        else:
            raise AssertionError(f"Unsupported character: {char}")
            # Raise an error if the character is unsupported
    return ' '.join(morse_code).strip()
    # Join the Morse codes and remove the trailing space


def main():
    # Check the number of command line arguments
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")
        # Raise an error if there are more or less than one argument

    input_string = sys.argv[1]  # Get the command line argument

    # Check if the input is only alphanumeric or contains spaces
    if not all(char.isalnum() or char.isspace() for char in input_string):
        raise AssertionError("the arguments are bad")
        # Raise an error if there are invalid characters

    # If the input is valid, proceed with Morse code encoding
    morse_result = encode_to_morse(input_string)  # Call the encoding function

    print(morse_result, end='')
    # Print the result without an additional newline


if __name__ == "__main__":
    try:
        main()  # Call the main function
    except AssertionError as error:
        print(error)  # Print any assertion error that occurs
