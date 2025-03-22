def create_dict_from_list():
    # Lista de tuplas proporcionada en las instrucciones
    d = [
        ('Hendrix', '1942'),
        ('Allman', '1946'),
        ('King', '1925'),
        ('Clapton', '1945'),
        ('Johnson', '1911'),
        ('Berry', '1926'),
        ('Vaughan', '1954'),
        ('Cooder', '1947'),
        ('Page', '1944'),
        ('Richards', '1943'),
        ('Hammett', '1962'),
        ('Cobain', '1967'),
        ('Garcia', '1942'),
        ('Beck', '1944'),
        ('Santana', '1947'),
        ('Ramone', '1948'),
        ('White', '1975'),
        ('Frusciante', '1970'),
        ('Thompson', '1949'),
        ('Burton', '1939')
    ]

    # Crear un diccionario donde el año es la clave y el nombre del músico es el valor
    # Si varios músicos tienen el mismo año, se concatenarán con un espacio
    musician_dict = {}  # Crear un diccionario vacío para almacenar los músicos agrupados por año.

    # Recorrer iterando la lista de tuplas `d`, donde cada tupla contiene un nombre y un año.
    for name, year in d:
        if year in musician_dict:  # Si el año ya existe como clave en el diccionario...
            musician_dict[year] += f" {name}"  # Concatenar el nombre actual al valor existente, separado por 
            # un espacio.f antes de name hace que se sustituya {name}" por el nombre de la tupla
        else:  # Si el año no está en el diccionario...
            musician_dict[year] = name  # Crear una nueva entrada con el año como clave y el nombre como valor.

    # Recorrer los elementos del diccionario para imprimirlos en el formato requerido.
    for year, names in musician_dict.items():
        print(f"{year} : {names}")  # Imprimir cada año seguido de los nombres correspondientes.

# Llamar a la función cuando el script se ejecuta directamente
if __name__ == '__main__':
    create_dict_from_list()



# El orden final no tendrá que ser el mismo que en el ejemplo. 
# Es un comportamiento habitual.
#¿Sabes por qué?  el orden dependerá del momento y método de inserción. 
# Para garantizar un orden específico, es necesario usar herramientas 
# como sorted() o estructuras como OrderedDict
