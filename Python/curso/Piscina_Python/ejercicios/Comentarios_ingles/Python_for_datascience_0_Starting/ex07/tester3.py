
##Traductor morse a texto y texto a morse

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

# Definir el diccionario inverso para convertir de Morse a texto
MORSE_TO_TEXT_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def morse_to_text(morse_code):
    """Convierte código Morse a texto."""
    text = []
    morse_words = morse_code.split(' / ')  # '/' separa las palabras en Morse
    for morse_word in morse_words:
        morse_chars = morse_word.split()  # Espacio separa caracteres en Morse
        word = ''.join(MORSE_TO_TEXT_DICT.get(char, '') for char in morse_chars)
        text.append(word)
    return ' '.join(text)

def text_to_morse(text):
    """Convierte texto a código Morse."""
    morse_code = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
    return ' '.join(morse_code)

if __name__ == "__main__":
    # Opción para que el usuario elija entre texto a Morse o Morse a texto
    choice = input("¿Deseas convertir (1) Texto a Morse o (2) Morse a Texto? Ingresa 1 o 2: ")

    if choice == '1':
        input_text = input("Ingresa el texto a traducir a Morse: ")
        morse_translation = text_to_morse(input_text)
        print(f"Texto original: {input_text}")
        print(f"Traducción en Morse: {morse_translation}")
    
    elif choice == '2':
        input_morse = input("Ingresa el código Morse a traducir: ")
        text_translation = morse_to_text(input_morse)
        print(f"Código Morse original: {input_morse}")
        print(f"Traducción en texto: {text_translation}")
    
    else:
        print("Opción no válida. Por favor, ingresa 1 o 2.")
