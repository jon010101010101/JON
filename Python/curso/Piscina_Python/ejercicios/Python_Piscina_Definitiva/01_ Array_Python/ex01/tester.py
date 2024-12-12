from array2D import slice_me

# Llamadas a la función slide para realizar pruebas
ffamily = [
    [1.80, 78.4],  # Índice 0   -3 Índice 
    [2.15, 102.7], # Índice 1   -2
    [2.10, 98.5],  # Índice 2   -1
    [1.88, 75.2]   # Índice 3    0
]


print(slice_me(family, 0, 2))
# Debería devolver las dos primeras filas por que start = 0 y end=2
print(slice_me(family, 1, -2)) 
# Debería devolver desde la segunda fila hasta la penúltima, por que
#start es 1 [2.15, 102.7], y end es -2. Con negativos se cuenta desde abajo
#end -2 es [2.15, 102.7],

