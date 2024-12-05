
    
#Toma un array 2D, imprime su forma y devuelve una versión truncada usando los 
# parámetros start y end.
#Maneja errores si las listas no son del mismo tamaño o no son listas.
 
# Toma un array 2D, imprime su forma y devuelve una versión truncada usando los 
# parámetros start y end.
# Maneja errores si las listas no son del mismo tamaño o no son listas.

def slice_me(family: list, start: int, end: int) -> list:
    # Verificar si 'family' es una lista 2D válida
    if not isinstance(family, list) or not all(isinstance(row, list) for row in family):
    #isinstance(family, list) vrifica si family es de clase list
    # all comprueba que todos los elementos cumplen. 
    # Si alguna de las filas no es lista devuelve false, si no true. 
        raise TypeError("Input must be a 2D list")
    
    # Verificar que todas las filas tengan la misma longitud
    row_lengths = [len(row) for row in family]
    #calcula el nuero de row que tiene la family, en este caso 2 cada fila
    if len(set(row_lengths)) != 1:
    #verifica si todas las row_lengths son iguales
        raise ValueError("All rows must have the same length")
    #raise es generar acción
    
    # Imprimir la forma del array 2D
    rows = len(family)
    cols = row_lengths[0] #0 es primer elemento
    # Forma en términos de filas y columnas
    print(f"My shape is : ({rows}, {cols})") 
    #la forma que tiene en filas y columnas
    
    # Aplicar el slicing (recortar o dividir algo en partes mas pequeñas)
    # en el array 2D usando los índices proporcionados
    # quita las filas que no son. si es 0,2 deberia devolver las dos priemras filas
    truncated = family[start:end]
    
    # Obtener la nueva forma del array truncado
    new_rows = len(truncated) #calcula el nº en truncated y lo asigna a row
    new_cols = cols if truncated else 0 #verifica que truncated no esta vacio. 
    #Si es O new_cols es = y si no da cols
    print(f"My new shape is : ({new_rows}, {new_cols})")
    
    return truncated





