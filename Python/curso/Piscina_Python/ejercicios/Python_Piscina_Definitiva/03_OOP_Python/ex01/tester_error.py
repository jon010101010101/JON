from S1E9 import Stark
from S1E7 import Baratheon, Lannister

if __name__ == "__main__":
    # Prueba 1: Intentar crear un Stark con un nombre vacío
    input1 = ""
    print(f"Test 1: Stark con input: '{input1}'")
    try:
        empty_name_stark = Stark(input1)  # Esto debería lanzar ValueError
    except ValueError as e:
        print(f"Caught expected error: {e}")  # Debería mostrar: "First name must be a non-empty string."

    # Prueba 2: Intentar crear un Stark con is_alive no booleano
    input2_name = "Invalid"
    input2_is_alive = "Not a boolean"
    print(f"\nTest 2: Stark con input: '{input2_name}', is_alive: '{input2_is_alive}'")
    try:
        invalid_stark = Stark(input2_name, is_alive=input2_is_alive)  # Esto debería lanzar TypeError
    except TypeError as e:
        print(f"Caught expected error: {e}")  # Debería mostrar: "is_alive must be a boolean."

    # Prueba 3: Intentar crear una instancia válida de Stark pero con is_alive no booleano
    input3_name = "Ned"
    input3_is_alive = "yes"
    print(f"\nTest 3: Stark con input: '{input3_name}', is_alive: '{input3_is_alive}'")
    try:
        ned_invalid = Stark(input3_name, is_alive=input3_is_alive)  # Esto debería lanzar TypeError
    except TypeError as e:
        print(f"Caught expected error: {e}")  # Debería mostrar: "is_alive must be a boolean."

    # Prueba 1: Intentar crear un Baratheon con un nombre vacío
    print("Test 4: Baratheon con un nombre vacío")
    try:
        empty_name_baratheon = Baratheon("")  # Esto debería lanzar ValueError
    except ValueError as e:
        print(f"Caught expected error: {e}")  # Debería mostrar: "First name must be a non-empty string."

    # Prueba 2: Intentar crear un Lannister con is_alive no booleano
    print("\nTest 5: Lannister con is_alive no booleano")
    try:
        invalid_lannister = Lannister("Cersei", is_alive="Not a boolean")  # Esto debería lanzar TypeError
    except TypeError as e:
        print(f"Caught expected error: {e}")  # Debería mostrar: "is_alive must be a boolean."

    # Prueba 3: Intentar crear un Baratheon con is_alive no booleano
    print("\nTest 6: Baratheon con is_alive no booleano")
    try:
        invalid_baratheon = Baratheon("Robert", is_alive="yes")  # Esto debería lanzar TypeError
    except TypeError as e:
        print(f"Caught expected error: {e}")  # Debería mostrar: "is_alive must be a boolean."

