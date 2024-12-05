def ft_filter(func, iterable):
    """
    Filtra los elementos del iterable según la función proporcionada.
    
    Args:
        func: Función que determina si un elemento debe ser incluido.
        iterable: Iterable a filtrar.

    Returns:
        List de elementos que cumplen la condición.
    """
    return [item for item in iterable if func(item)] #lista de compresion

    # Usa una lista de comprensión: [item for item in iterable if func(item)]

    #Esto crea una nueva lista con los elementos de iterable que cumplen la 
    # condición definida por func.

    #La función func se aplica a cada item en el iterable.
    #Solo los elementos para los que func(item) devuelve True se incluyen en 
    # la lista resultante.
    #La docstring proporciona una descripción clara de lo que hace la función
    #  y sus parámetros.