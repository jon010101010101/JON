from ft_calculator import calculator  # Asegúrate de que esto apunte al archivo correcto

if __name__ == "__main__":
    # Prueba 1: Intentar crear un calculator con un input que no es una lista
    input1 = "not a list"
    print(f"Test 1: Calculator con input: {input1}")
    try:
        calc = calculator(input1)  # Esto debería lanzar TypeError
    except TypeError as e:
        print(f"Caught expected error: {e}")  # Debería mostrar: "Input must be a list."

    # Prueba 2: Intentar crear un calculator con una lista vacía
    input2 = []
    print(f"\nTest 2: Calculator con input: {input2}")
    try:
        calc = calculator(input2)  # Esto debería lanzar ValueError
    except ValueError as e:
        print(f"Caught expected error: {e}")  # Debería mostrar: "Vector cannot be empty."

    # Prueba 3: Intentar crear un calculator con elementos no numéricos
    input3 = [1, 2, 'three']
    print(f"\nTest 3: Calculator con input: {input3}")
    try:
        calc = calculator(input3)  # Esto debería lanzar ValueError
    except ValueError as e:
        print(f"Caught expected error: {e}")  # Debería mostrar: "All elements must be numeric."

    # Prueba 4: Intentar dividir por cero
    print("\nTest 4: Dividir por cero")
    try:
        valid_calc = calculator([1, 2, 3])  # Esto debería funcionar sin errores
        valid_calc / 0  # Esto debería lanzar ZeroDivisionError
    except ZeroDivisionError as e:
        print(f"Caught expected error: {e}")  # Debería mostrar el mensaje de error esperado.

