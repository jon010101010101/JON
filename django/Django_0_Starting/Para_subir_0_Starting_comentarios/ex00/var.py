def my_var():
    # Entero
    a = 42
    print(f"{a} has a type {type(a)}")
    
    # String numérico
    b = "42"
    print(f"{b} has a type {type(b)}")
    
    # String en francés
    c = "quarante-deux"
    print(f"{c} has a type {type(c)}")
    
    # Flotante
    d = 42.0
    print(f"{d} has a type {type(d)}")
    
    # Booleano
    e = True
    print(f"{e} has a type {type(e)}")
    
    # Lista
    f = [42]
    print(f"{f} has a type {type(f)}")
    
    # Diccionario
    g = {42: 42}
    print(f"{g} has a type {type(g)}")
    
    # Tupla (necesita la coma para ser tupla)
    h = (42,)
    print(f"{h} has a type {type(h)}")
    
    # Conjunto vacío
    i = set()
    print(f"{i} has a type {type(i)}")

if __name__ == '__main__':
    my_var()
