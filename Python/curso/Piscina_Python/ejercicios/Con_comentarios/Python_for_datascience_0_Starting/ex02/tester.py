from find_ft_type import all_thing_is_obj

# Variable definitions to test the function
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Calls the function with different types of objects
all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")

# Calls the function with an integer
#print(all_thing_is_obj(15))

# Calls the function with an integer, which
# will print the type of int and then show 42 with $
print(all_thing_is_obj(10))

# It uses 10 because it indicates the exercise, but it would do the same
# with another integer, e.g., 15.

