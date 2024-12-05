import sys


def to_morse_code(text):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/',
    }
    morse_code = []
    for char in text.upper():
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        else:
            raise AssertionError("AssertionError: the arguments are bad ")
    return ' '.join(morse_code)


def main():
    try:
        if len(sys.argv) != 2 or len(sys.argv[1]) == 0 or not isinstance(
                sys.argv[1], str):
            raise AssertionError("Usage: python3.10 morse_encoder.py <text>")
        input_text = sys.argv[1]
        morse_result = to_morse_code(input_text)
        print(morse_result)
    except AssertionError as error:
        print(error)


if __name__ == "__main__":
    main()
