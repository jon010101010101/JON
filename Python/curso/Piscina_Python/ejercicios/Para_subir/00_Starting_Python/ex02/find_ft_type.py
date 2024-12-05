""""Prints the type of the object and returns 42."""

def all_thing_is_obj(obj: any) -> int:
    """Checks the type of the given object and prints the result."""
    
    # Define a dictionary to map types to messages
    type_messages = {
        list: f"List : {type(obj)}",
        tuple: f"Tuple : {type(obj)}",
        set: f"Set : {type(obj)}",
        dict: f"Dict : {type(obj)}",
        str: f"{obj} is in the kitchen : {type(obj)}",
        type(None): "Nothing: None <class 'NoneType'>",
        float: "Cheese: nan <class 'float'>" if (obj != obj) else None,
        bool: f"Fake: {obj} <class 'bool'>"
    }
    
    # Check the type of the object and get the corresponding message
    for type_key, message in type_messages.items():
        # The dictionary is composed of Type Key and associated message
        # type_messages.items() returns (list, "List : <class 'list'>$") or tuple, etc.
        if isinstance(obj, type_key):
            # isinstance(obj, type_key): This function checks if obj is an instance of
            # the type represented by type_key. If obj is of the type that corresponds to type_key,
            # the code block inside this if statement is executed.

            if message:  # to ensure it is not None
                print(message)
            return 42

    print("Type not found$")
    return 42
