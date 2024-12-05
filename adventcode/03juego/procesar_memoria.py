import re

def procesar_memoria(cadena):
    # Expresión regular para encontrar las instrucciones válidas "mul(X,Y)"
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
    
    # Buscar todas las coincidencias de las instrucciones
    instrucciones = re.findall(pattern, cadena)
    
    # Inicializar la suma total
    total = 0
    habilitado = True  # Las multiplicaciones están habilitadas al principio
    
    # Procesar cada instrucción
    for instruccion in instrucciones:
        if instruccion == ('do()', ''):
            habilitado = True  # Habilitar las multiplicaciones futuras
        elif instruccion == ("don't()", ""):
            habilitado = False  # Deshabilitar las multiplicaciones futuras
        elif instruccion[0]:  # Es una instrucción "mul(X,Y)"
            x, y = map(int, instruccion)  # Convertir los valores a enteros
            if habilitado:  # Solo ejecutar si las multiplicaciones están habilitadas
                total += x * y  # Multiplicar y sumar al resultado
    
    return total

# Ejemplo de uso
if __name__ == "__main__":
    # Leer los datos del archivo "input03juego"
    with open("input03juego", "r") as file:
        cadena_memoria = file.read()  # Leer todo el contenido del archivo
    
    resultado = procesar_memoria(cadena_memoria)
    print(f"Resultado final: {resultado}")


