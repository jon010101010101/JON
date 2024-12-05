#Tester de comprobacion traduccion a morse

def morse_code(text):
    # Definición del código Morse
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
        'Z': '--..', 
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
        '8': '---..', '9': '----.', ' ': '/'
    }
    
    # Convertir el texto a mayúsculas y eliminar caracteres no soportados
    text = text.upper()
    result = []
    unsupported_chars = []  # Lista para almacenar caracteres no soportados
    
    for char in text:
        if char in morse_dict:
            result.append(morse_dict[char])
        else:
            unsupported_chars.append(char)  # Agregar a la lista de caracteres no soportados
    
    # Si hay caracteres no soportados, el resultado Morse es vacío
    if unsupported_chars:
        return '', unsupported_chars
    
    morse_result = ' '.join(result)  # Juntar el resultado en una cadena
    return morse_result, unsupported_chars

# Casos de prueba
test_cases = [
    ("Hello World", ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."),
    ("Peter is not coming?", ""),  # Esperado: vacío porque hay un '?'
    ("42", "....- ..---"),
    ("Urduliz", "..- .-. -.. ..- .-.. .. --.."),
    ("%&**", ""),  # Esperado: vacío porque hay caracteres no soportados
    ("si algo me gusta es poder buscar la palabra sin acentos y encontrar textos sin acentos que poder escribir y escribir texto sin parar ademas que ya no miro el teclado para nada",
     "... .. / .- .-.. --. --- / -- . / --. ..- ... - .- / . ... / .--. --- -.. . .-. / -... ..- ... -.-. .- .-. / .-.. .- / .--. .- .-.. .- -... .-. .- / ... .. -. / .- -.-. . -. - --- ... / -.-- / . -. -.-. --- -. - .-. .- .-. / - . -..- - --- ... / ... .. -. / .- -.-. . -. - --- ... / --.- ..- . / .--. --- -.. . .-. / . ... -.-. .-. .. -... .. .-. / -.-- / . ... -.-. .-. .. -... .. .-. / - . -..- - --- / ... .. -. / .--. .- .-. .- .-. / .- -.. . -- .- ... / --.- ..- . / -.-- .- / -. --- / -- .. .-. --- / . .-.. / - . -.-. .-.. .- -.. --- / .--. .- .-. .- / -. .- -.. .-")
]

# Ejecutar las pruebas
all_passed = True

for i, (input_text, expected) in enumerate(test_cases):
    result, unsupported = morse_code(input_text)
    print(f"Test Case {i + 1}: {'Passed' if result == expected else 'Failed'}")
    print(f"  Input: {input_text}")
    print(f"  Expected: {expected}")
    print(f"  Result: {result}")
    
    # Mostrar caracteres no soportados
    if unsupported:
        print(f"  Unsupported characters omitted: {', '.join(unsupported)}")

    if result != expected:
        all_passed = False

if all_passed:
    print("The test has passed correctly.")
else:
    print("The test has not passed completely.")
