import re

def procesar_memoria(cadena):
    # Expresión regular para encontrar las instrucciones válidas "mul(X,Y)"
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    # Buscar todas las coincidencias válidas de multiplicación
    matches = re.findall(pattern, cadena)
    
    # Inicializar la suma total
    total = 0
    
    # Sumar los resultados de cada multiplicación
    for match in matches:
        x, y = map(int, match)  # Convertir los valores a enteros
        total += x * y  # Multiplicar y sumar el resultado
    
    return total

# Ejemplo de uso
if __name__ == "__main__":
    # Leer los datos del archivo "input03juego"
    with open("input03juego", "r") as file:
        cadena_memoria = file.read()  # Leer todo el contenido del archivo
    
    resultado = procesar_memoria(cadena_memoria)
    print(f"Resultado final: {resultado}")

