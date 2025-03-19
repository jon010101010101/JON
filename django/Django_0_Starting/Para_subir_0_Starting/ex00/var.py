def my_var():
    # Integer
    a = 42
    print(f"{a} has a type {type(a)}")
    
    # Numeric string
    b = "42"
    print(f"{b} has a type {type(b)}")
    
    # French string
    c = "quarante-deux"
    print(f"{c} has a type {type(c)}")
    
    # Float
    d = 42.0
    print(f"{d} has a type {type(d)}")
    
    # Boolean
    e = True
    print(f"{e} has a type {type(e)}")
    
    # List
    f = [42]
    print(f"{f} has a type {type(f)}")
    
    # Dictionary
    g = {42: 42}
    print(f"{g} has a type {type(g)}")
    
    # Tuple (needs a comma to be a tuple)
    h = (42,)
    print(f"{h} has a type {type(h)}")
    
    # Empty set
    i = set()
    print(f"{i} has a type {type(i)}")

if __name__ == '__main__':
    my_var()

