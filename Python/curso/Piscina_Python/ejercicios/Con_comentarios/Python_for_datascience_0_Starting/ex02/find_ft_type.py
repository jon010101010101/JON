""""Prints the type of the object and returns 42."""

def all_thing_is_obj(obj: any) -> int:
    """Checks the type of the given object and prints the result."""
    
    # Define un diccionario para mapear tipos a mensajes
    type_messages = {
        list: f"List : {type(obj)}$",
        tuple: f"Tuple : {type(obj)}$",
        set: f"Set : {type(obj)}$",
        dict: f"Dict : {type(obj)}$",
        str: f"{obj} is in the kitchen : {type(obj)}$",
        type(None): "Nothing: None <class 'NoneType'>$",
        float: "Cheese: nan <class 'float'>$" if (obj != obj) else None,
        bool: f"Fake: {obj} <class 'bool'>$"
    }
    
    # Verifica el tipo del objeto y obtiene el mensaje correspondiente
    for type_key, message in type_messages.items():
    # El diccionario se compoone de Type Key y message asociado
    #type_messages.items(). devuleve (list, "List : <class 'list'>$") o tupla etc
        if isinstance(obj, type_key):
    #isinstance(obj, type_key): Esta función comprueba si obj es una instancia del
    #  tipo representado por type_key. Si obj es del tipo que corresponde a type_key,
    #  el bloque de código dentro de este if se ejecuta.

            if message:  # para asegurarse de que no sea None
                print(message)
            return 42  # Siempre devuelve 42

    print("Type not found$")
    return 42  # Siempre devuelve 42


