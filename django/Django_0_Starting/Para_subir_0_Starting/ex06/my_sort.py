# Dictionary of musicians with their birth years
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

# Sort the dictionary items
# Key function: (birth year as integer, name)
# The lambda reverses each tuple, for ('Hendrix', '1942'),
# it returns (1942, 'Hendrix').
sorted_musicians = sorted(d.items(), key=lambda x: (int(x[1]), x[0]))

# Print each musician's name in the sorted order
for musician in sorted_musicians:
    print(musician[0])
