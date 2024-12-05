# Inicializa las estructuras de datos
ft_list = ["Hola", "tata!"]
ft_tuple = ("Hola", "toto!")
ft_set = {"Hola", "tutu!"}
ft_dict = {"Hola": "titi!"}

# Modifica la lista
ft_list[1] = "Mundo!"  # Cambia "tata!" por "Mundo!"

# Modifica la tupla (las tuplas son inmutables, se crea una nueva)
ft_tuple = (ft_tuple[0], "España!")  # Cambia "toto!" por "España!"

# Modifica el conjunto
ft_set.remove("tutu!")  # Elimina "tutu!"
ft_set.add("Urduliz!")  # Añade "Urduliz!"

# Modifica el diccionario
ft_dict["Hola"] = "42Urduliz!"  # Cambia el valor asociado a "Hola"

# Imprime los resultados
print(ft_list)    # Salida: ['Hola', 'Mundo!']
print(ft_tuple)   # Salida: ('Hola', 'España!')
print(ft_set)     # Salida: {'Hola', 'Urduliz!'}
print(ft_dict)    # Salida: {'Hola': '42Urduliz!'}



