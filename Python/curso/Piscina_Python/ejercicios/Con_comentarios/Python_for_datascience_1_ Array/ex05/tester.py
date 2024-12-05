from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

# Cargar una imagen de ejemplo
array = ft_load("landscape.jpg")

# Aplicar filtros de color
imagen_invertida = ft_invert(array)
imagen_roja = ft_red(array)
imagen_verde = ft_green(array)
imagen_azul = ft_blue(array)
imagen_gris = ft_grey(array)

# Imprimir el docstring de la función de inversión
print(ft_invert.__doc__)
