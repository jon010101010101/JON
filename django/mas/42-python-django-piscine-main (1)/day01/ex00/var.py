def my_var():
	var = 42
	var_str = "42"
	var_deux = "quarante-deux"
	var_float = 42.0
	var_true = True
	var_list = [42]
	var_dict = {42: 42}
	var_tuple = (42, )
	var_set = set()
	print(var, "has a type ", type(var))
	print(var_str, "has a type ", type(var_str))
	print(var_deux, "has a type ", type(var_deux))
	print(var_float, "has a type ", type(var_float))
	print(var_true, "has a type ", type(var_true))
	print(var_list, "has a type ", type(var_list))
	print(var_dict, "has a type ", type(var_dict))
	print(var_tuple, "has a type ", type(var_tuple))
	print(var_set, "has a type ", type(var_set))


if __name__ == "__main__":
	my_var()
