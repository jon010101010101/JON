
def give_bmi(height: list[int | float], weight: list[int | float]) -> list[float]:
    # Verificar que ambas listas tienen el mismo tamaño
    if len(height) != len(weight):
        raise ValueError("Las listas de altura y peso deben tener el mismo tamaño.")
    
    # Verificar que todos los elementos son números
    # La función isinstance() en Python se utiliza para verificar si un objeto es una instancia de una clase o de
    #  una subclase de esa clase. A continuación, se explica su funcionamiento
    #  y uso.
    if not all(isinstance(h, (int, float)) for h in height) or not all(isinstance(w, (int, float)) for w in weight):
        raise TypeError("Los elementos de las listas deben ser enteros o flotantes.")
    #all. toodos tiene que ser True, y hay uno False, es false
    # (isinstance(h, (int, float)) for h in height), comprueba que cada
    #elemento heigt es un numero (int o float)
    # verifica si: Al menos un elemento en la lista height no es un número
    #  (entero o flotante). O al menos un elemento en la lista weight no es
    #  un número (entero o flotante).


    # Calcular el BMI: BMI = peso / (altura ^ 2). For hace bucle entre h y w
    # Zip convina dos listas.si height = [1.75, 1.80] y weight = [70, 80], zip 
    # crearía pares como (1.75, 70) y (1.80, 80).
    bmi = [w / (h ** 2) for h, w in zip(height, weight)]
    return bmi

# give_bmi: Toma dos listas, height y weight, y calcula el índice de masa
#  corporal (BMI) con la fórmula BMI = peso / altura^2. Verifica que las
#  listas tengan el mismo tamaño y que todos los elementos sean números
#  (int o float).

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    # Aplica un limite a los valors proporcionados. 
    # Verifica que los elementos son números (int o float)
    #Si no todoss los elementos de bmi son int o float cumple la condicion
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise TypeError("Los valores de BMI deben ser enteros o flotantes.")
    
    # Retornar una lista de booleanos según el límite
    return [b > limit for b in bmi]

    #apply_limit: Toma la lista de BMI calculada y un límite. Devuelve 
    # una lista de valores booleanos (True si el BMI está por encima del
    #  límite, False si no)
