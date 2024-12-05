from S1E9 import Stark
from S1E7 import Baratheon, Lannister
from DiamondTrap import King

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

    # Prueba 4: Intentar crear un Baratheon con un nombre vacío
    input4 = ""
    print(f"\nTest 4: Baratheon con input: '{input4}'")
    try:
        empty_name_baratheon = Baratheon(input4)  # Esto debería lanzar ValueError
    except ValueError as e:
        print(f"Caught expected error: {e}")  # Debería mostrar: "First name must be a non-empty string."

    # Prueba 5: Intentar crear un Lannister con is_alive no booleano
    input5_name = "Cersei"
    input5_is_alive = "Not a boolean"
    print(f"\nTest 5: Lannister con input: '{input5_name}', is_alive: '{input5_is_alive}'")
    try:
        invalid_lannister = Lannister(input5_name, is_alive=input5_is_alive)  # Esto debería lanzar TypeError
    except TypeError as e:
        print(f"Caught expected error: {e}")  # Debería mostrar: "is_alive must be a boolean."

    # Prueba 6: Intentar crear un Baratheon con is_alive no booleano
    input6_name = "Robert"
    input6_is_alive = "yes"
    print(f"\nTest 6: Baratheon con input: '{input6_name}', is_alive: '{input6_is_alive}'")
    try:
        invalid_baratheon = Baratheon(input6_name, is_alive=input6_is_alive)  # Esto debería lanzar TypeError
    except TypeError as e:
        print(f"Caught expected error: {e}")  # Debería mostrar: "is_alive must be a boolean."

    # Prueba 7: Intentar crear un King con un nombre vacío
    input7 = ""
    print(f"\nTest 7: King con input: '{input7}'")
    try:
        empty_name_king = King(input7)  # Esto debería lanzar ValueError
        print("Error: No se lanzó ValueError para nombre vacío.")
    except ValueError as e:
        print(f"Caught expected error: {e}")  # Debería mostrar el mensaje de error esperado.

    # Prueba 8: Intentar crear un King con is_alive no booleano (heredado de Baratheon)
    input8_name = "Joffrey"
    input8_is_alive = "Not a boolean"
    print(f"\nTest 8: King con input: '{input8_name}', is_alive: '{input8_is_alive}'")
    try:
        invalid_king = King(input8_name, is_alive=input8_is_alive)  # Esto debería lanzar TypeError
        print("Error: No se lanzó TypeError para is_alive no booleano.")
    except TypeError as e:
        print(f"Caught expected error: {e}")  # Debería mostrar el mensaje de error esperado.

    # Prueba 9: Intentar crear un King con is_alive no booleano (heredado de Lannister)
    input9_name = "Tommen"
    input9_is_alive = "yes"
    print(f"\nTest 9: King con input: '{input9_name}', is_alive: '{input9_is_alive}'")
    try:
        invalid_king_lannister = King(input9_name, is_alive=input9_is_alive)  # Esto debería lanzar TypeError
        print("Error: No se lanzó TypeError para is_alive no booleano.")
    except TypeError as e:
        print(f"Caught expected error: {e}")  # Debería mostrar el mensaje de error esperado.
