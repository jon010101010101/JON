import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

# Cargar la imagen
array = ft_load("landscape.jpg")

# Aplicar filtros
inverted = ft_invert(array)
red_filtered = ft_red(array)
green_filtered = ft_green(array)
blue_filtered = ft_blue(array)
grey_filtered = ft_grey(array)

# Mostrar imágenes en dos filas y tres columnas
filters = [
    (array, "Figura VIII.1: Original"),
    (inverted, "Figura VIII.2: Invert"),
    (red_filtered, "Figura VIII.3: Red"),
    (green_filtered, "Figura VIII.4: Green"),
    (blue_filtered, "Figura VIII.5: Blue"),
    (grey_filtered, "Figura VIII.6: Grey")
]

fig, axs = plt.subplots(2, 3, figsize=(15, 10))

for ax, (img, title) in zip(axs.flatten(), filters):
    ax.imshow(img)
    ax.axis('off')  # Ocultar los ejes
    # Título debajo de la imagen
    plt.text(0.5, -0.1, title, fontsize=10, ha='center', va='top', transform=ax.transAxes)

plt.tight_layout()  # Ajustar el espaciado
plt.show()  # Mostrar todas las imágenes


