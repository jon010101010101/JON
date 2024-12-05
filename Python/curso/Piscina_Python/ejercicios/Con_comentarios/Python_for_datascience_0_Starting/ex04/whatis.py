"""Crea un script que tome un número como argumento, verifique si es par o impar, y
imprima el resultado.
Si se proporciona más de un argumento o si el argumento no es un entero, imprime un AssertionError.
"""
import sys  # Importa el módulo sys

def main():  # Punto de entrada del programa
    # Verifica si se proporciona exactamente un argumento
    if len(sys.argv) != 2:  # Comprueba cuántos argumentos se pasan
        if len(sys.argv) > 2:  # Si hay más de dos argumentos
            raise AssertionError("se proporciona más de un argumento")
        else:
            print('$')  # Imprime solo un signo de dólar
            return  # Termina la función si no se proporciona ningún argumento

    # Intenta convertir el argumento a un entero
    try:  # Comienza a ejecutar el código
        numero = int(sys.argv[1])  # Intenta convertir el primer argumento a un entero
    except ValueError:
        raise AssertionError("el argumento no es un entero")

    # Verifica si el número es par o impar
    if numero % 2 == 0:
        print("Soy Par.")
    else:
        print("Soy Impar.")

# Esta línea verifica si el script se está ejecutando directamente
# (no importado como un módulo en otro script). Si es así, llama
# a la función main() para iniciar la ejecución del programa.

if __name__ == "__main__":
    main()


