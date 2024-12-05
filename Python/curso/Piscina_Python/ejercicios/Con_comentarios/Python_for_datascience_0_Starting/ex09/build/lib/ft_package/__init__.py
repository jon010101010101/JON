from .count import count_in_list


"""
Acts as the entry point for the package. It could be inside count.py,
but it is usually placed this way because it facilitates imports when needed
or removes them.

This package does not have it, but it could have another module with more functions.

For example:

ft_package/
│
├── __init__.py  # Here you import the functions you want to expose
├── count.py     # Contains the function count_in_list
└── other_module.py  # Another module with more functions
"""
