def all_thing_is_obj(object: any) -> int:
    obj_type = type(object).__name__

    if obj_type in ['list', 'tuple', 'set', 'dict']:
        print(f"{obj_type.capitalize()} : <class '{obj_type}'>")
    elif obj_type == 'str':
        print(f"{object} is in the kitchen : <class 'str'>")
    else:
        print("Type not found")
    
    return 42
