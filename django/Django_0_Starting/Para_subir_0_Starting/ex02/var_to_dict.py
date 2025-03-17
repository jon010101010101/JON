def create_dict_from_list():
    # List of tuples as provided in the instructions
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

    # Create a dictionary where the year is the key and the musician's name is the value
    # If multiple musicians have the same year, they will be concatenated with a space
    musician_dict = {}
    for name, year in d:
        if year in musician_dict:
            musician_dict[year] += f" {name}"
        else:
            musician_dict[year] = name

    # Print the dictionary in the required format
    for year, names in musician_dict.items():
        print(f"{year} : {names}")


# Call the function when the script is executed directly
if __name__ == '__main__':
    create_dict_from_list()


# El orden final no tendrá que ser el mismo que en el ejemplo. 
# Es un comportamiento habitual.
#¿Sabes por qué?  el orden dependerá del momento y método de inserción. 
# Para garantizar un orden específico, es necesario usar herramientas 
# como sorted() o estructuras como OrderedDict
