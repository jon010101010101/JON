from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

# Load an example image
array = ft_load("landscape.jpg")

# Apply color filters
inverted_image = ft_invert(array)
red_image = ft_red(array)
green_image = ft_green(array)
blue_image = ft_blue(array)
grey_image = ft_grey(array)

# Print docstring for invert function
print(ft_invert.__doc__)


