def ft_filter(func, iterable):
    """
    Filtra los elementos del iterable según la función proporcionada.
    
    Args:
        func: Función que determina si un elemento debe ser incluido.
        iterable: Iterable a filtrar.

    Returns:
        List de elementos que cumplen la condición.
    """
    return [item for item in iterable if func(item)]
