
import math


def NULL_not_found(object: any) -> int:
    type_names = {
        None: "Nothing",
        math.nan: "Cheese",
        0: "Zero_Integer",
        '': "Empty_string",
        False: "Fake"
    }

    null_type = type_names.get(object, "Type not Found")

    if type(object) is float:
        print(f"Cheese: {object} {type(object)}")
    elif object == 0 and isinstance(object, int):
        print(f"Zero: {object} {type(object)}")
    elif object is None:
        print(f"Nothing: {object} {type(object)}")
    elif object == '':
        print(f"Empty: {object} {type(object)}")
    elif isinstance(object, bool):
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not Found")

    if null_type == "Type not Found":
        return 1

    return 0
