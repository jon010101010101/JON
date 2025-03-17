def read_and_print_numbers():
    try:
        # Abrir el archivo numbers.txt en modo lectura
        with open('numbers.txt', 'r') as file:
            # Leer el contenido del archivo
            content = file.read()
            
            # Dividir el contenido por comas
            numbers = content.split(',')
            
            # Imprimir cada número en una línea separada
            for number in numbers:
                # strip() elimina espacios en blanco al inicio y al final
                print(number.strip())
    
    except FileNotFoundError:
        print("Error: El archivo 'numbers.txt' no se encontró.")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Llamar a la función cuando se ejecute el script
if __name__ == '__main__':
    read_and_print_numbers()
