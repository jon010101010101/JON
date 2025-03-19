def create_dict_from_list():
    # List of tuples provided in the instructions
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

    # Iterate through the list of tuples `d`, where each tuple contains a name and a year
    for name, year in d:
        if year in musician_dict:
            musician_dict[year] += f" {name}"  # Concatenate the current name to the existing value, separated by a space
        else:
            musician_dict[year] = name

    # Iterate through the dictionary items to print them in the required format
    for year, names in musician_dict.items():
        print(f"{year} : {names}")

# Call the function when the script is executed directly
if __name__ == '__main__':
    create_dict_from_list()


