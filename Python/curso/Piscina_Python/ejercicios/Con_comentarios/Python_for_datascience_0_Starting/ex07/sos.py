import sys

# Diccionario que contiene las representaciones en código Morse
NESTED_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'  # El espacio se representa como /
}


def encode_to_morse(cadena_entrada):
    """Codifica la cadena de entrada a código Morse."""
    codigo_morse = []  # Lista para almacenar el código Morse
    for caracter in cadena_entrada.upper():  # Convertir a mayúsculas para consistencia
        if caracter in NESTED_MORSE:  # Comprobar si el carácter está en el diccionario
            codigo_morse.append(NESTED_MORSE[caracter])  # Añadir el código
            # Morse correspondiente
        else:
            raise AssertionError(f"Carácter no soportado: {caracter}")
            # Lanzar un error si el carácter no está soportado
    return ' '.join(codigo_morse).strip()
    # Unir los códigos Morse y eliminar el espacio final


def main():
    # Comprobar el número de argumentos de línea de comandos
    if len(sys.argv) != 2:
        raise AssertionError("los argumentos son incorrectos")
        # Lanzar un error si hay más o menos de un argumento

    cadena_entrada = sys.argv[1]  # Obtener el argumento de línea de comandos

    # Comprobar si la entrada es solo alfanumérica o contiene espacios
    if not all(caracter.isalnum() or caracter.isspace() for caracter in cadena_entrada):
        raise AssertionError("los argumentos son incorrectos")
        # Lanzar un error si hay caracteres inválidos

    # Si la entrada es válida, proceder con la codificación Morse
    resultado_morse = encode_to_morse(cadena_entrada)  # Llamar a la función de codificación

    print(resultado_morse, end='')
    # Imprimir el resultado sin un salto de línea adicional


if __name__ == "__main__":
    try:
        main()  # Llamar a la función principal
    except AssertionError as error:
        print(error)  # Imprimir cualquier error de aserción que ocurra

