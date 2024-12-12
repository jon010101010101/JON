# Initialize the data structures
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Modify the list
ft_list[1] = "World!"  # Change "tata!" to "World!"

# Modify the tuple (tuples are immutable, a new one is created)
ft_tuple = (ft_tuple[0], "Spain!")  # Change "toto!" to "Spain!"

# Modify the set
ft_set.remove("tutu!")  # Remove "tutu!"
ft_set.add("Urduliz!")  # Add "Urduliz!"

# Modify the dictionary
ft_dict["Hello"] = "42Urduliz!"  # Change the value associated with "Hello"

# Print the results
print(ft_list)    # Output: ['Hello', 'World!']
print(ft_tuple)   # Output: ('Hello', 'Spain!')
print(ft_set)     # Output: {'Hello', 'Urduliz!'}
print(ft_dict)    # Output: {'Hello': '42Urduliz!'}



