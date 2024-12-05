import sys
import string

def contar_caracteres(texto):
    """
    Cuenta el número de letras mayúsculas, minúsculas, signos de puntuación, espacios y dígitos en un texto dado.
    """
    return {
        ''upper': sum(1 for c in text if c.isupper()),
        'lower': sum(1 for c in text if c.islower()),
        'punctuation': sum(1 for c in text if c in string.punctuation),
        'spaces': sum(1 for c in text if c.isspace()),
        'digits': sum(1 for c in text if c.isdigit())
    }

def mostrar_conteos(texto, conteos):
    """
    Muestra los conteos de caracteres de manera formateada.
    """
    total_chars = len(text)
    output = f"The text contains {total_chars} characters:\n"
    output += f"{counts['upper']} upper letters\n"
    output += f"{counts['lower']} lower letters\n"
    output += f"{counts['punctuation']} punctuation marks\n"
    output += f"{counts['spaces']} spaces\n"
    output += f"{counts['digits']} digits"
    return output

def procesar_entrada(texto):
    """
    Procesa el texto de entrada contando sus caracteres y mostrando los resultados.
    """
    counts = count_characters(text)
    return display_counts(text, counts)

def main():
    """
    Función principal para manejar la entrada y procesarla.
    """
    if len(sys.argv) > 2:
        print("AssertionError: demasiados argumentos")
        return
    
    if len(sys.argv) == 2:
        texto = sys.argv[1].replace('\n', ' ').replace('-\n', '-')
    else:
        texto = input("¿Cuál es el texto a contar?\n")
        texto += '\n'  # Añadir nueva línea para el caso de entrada
    
    resultado = procesar_entrada(texto)
    print(resultado)

if __name__ == "__main__":
    main()









