# Diccionario de músicos con sus años de nacimiento
d = {
    'Hendrix': '1942',
    'Allman': '1946',
    'King': '1925',
    'Clapton': '1945',
    'Johnson': '1911',
    'Berry': '1926',
    'Vaughan': '1954',
    'Cooder': '1947',
    'Page': '1944',
    'Richards': '1943',
    'Hammett': '1962',
    'Cobain': '1967',
    'Garcia': '1942',
    'Beck': '1944',
    'Santana': '1947',
    'Ramone': '1948',
    'White': '1975',
    'Frusciante': '1970',
    'Thompson': '1949',
    'Burton': '1939',
}

# Ordenar los elementos del diccionario
# Función clave: (año de nacimiento como entero, nombre)
# Lambda es una pequeña función que indica como se tienen que ordenar primero por año (int(x[1])) 
# y si son del mismo año alfabeticamente por nombre (x)
# d.items(): Devuelve una lista de tuplas (clave, valor) del diccionario d. Cada tupla representa una entrada del diccionario.

#key=lambda x: (int(x[1]), x[0]): La función key determina cómo se comparan los elementos 
# en la lista de tuplas.
#x[1]: Es el valor de cada entrada del diccionario.
#int(x[1]): Convierte el valor a un número entero para que la ordenación se haga 
# numéricamente.
#x[0]: Es la clave de cada entrada del diccionario
# ordenando primero por el valor (como número entero) y, en caso de que dos valores sean iguales, se ordenará por la clave 
# (en orden alfabético).

# la lambda lo que hace es dar la vuelta a cada tupla, para ('Hendrix', '1942'), 
# devuelve (1942, 'Hendrix'). 
sorted_musicians = sorted(d.items(), key=lambda x: (int(x[1]), x[0]))

# Imprimir el nombre de cada músico en el orden ordenado
for musician in sorted_musicians:
    print(musician[0])
