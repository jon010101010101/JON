
#traductor Texto a morse

# Definimos un diccionario para la traducción a código Morse
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
    '0': '-----', ' ': '/',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', "'": '.----.', 
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', 
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', 
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', 
    '$': '...-..-', '@': '.--.-.'
}

def text_to_morse(text):
    """Convierte texto a código Morse."""
    morse_code = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
    return ' '.join(morse_code)

if __name__ == "__main__":
    input_text = input("Ingresa el texto a traducir a Morse: ")
    morse_translation = text_to_morse(input_text)

    print()  # Línea en blanco
    print(f"Texto original: {input_text}")
    print(f"Traducción en Morse: {morse_translation}")
    print("Fin de la traducción a morse.")
