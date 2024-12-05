from ft_calculator import calculator  # Asegúrate de que esto apunte al archivo correcto

if __name__ == "__main__":
    # Prueba 1: Intentar calcular el producto punto con inputs no listas
    input1 = "not a list"
    print(f"Test 1: Producto punto con input: {input1}")
    try:
        calculator.dotproduct(input1, [1, 2, 3])  # Esto debería lanzar TypeError
    except TypeError as e:
        print(f"Caught expected error: {e}")  # Debería mostrar: "Both inputs must be lists"

    # Prueba 2: Intentar calcular el producto punto con listas de diferente longitud
    input2_V1 = [1, 2]
    input2_V2 = [1, 2, 3]
    print(f"\nTest 2: Producto punto con inputs: {input2_V1} y {input2_V2}")
    try:
        calculator.dotproduct(input2_V1, input2_V2)  # Esto debería lanzar ValueError
    except ValueError as e:
        print(f"Caught expected error: {e}")  # Debería mostrar: "Vectors must have the same length"

    # Prueba 3: Intentar calcular el producto punto con elementos no numéricos
    input3_V1 = [1, 'two', 3]
    input3_V2 = [4, 5, 6]
    print(f"\nTest 3: Producto punto con inputs: {input3_V1} y {input3_V2}")
    try:
        calculator.dotproduct(input3_V1, input3_V2)  # Esto debería lanzar TypeError
    except TypeError as e:
        print(f"Caught expected error: {e}")  # Debería mostrar: "All elements must be numeric"

    # Prueba 4: Intentar sumar vectores con inputs no listas
    input4 = "not a list"
    print(f"\nTest 4: Sumar vectores con input: {input4}")
    try:
        calculator.add_vec(input4, [1, 2, 3])  # Esto debería lanzar TypeError
    except TypeError as e:
        print(f"Caught expected error: {e}")  # Debería mostrar: "Both inputs must be lists"
    