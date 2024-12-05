import pandas as pd

# pd es un alias comúnmente utilizado al importar la biblioteca.
# Este alias facilita el uso de las funciones y estructuras de datos
# de Pandas sin tener que escribir el nombre completo cada vez


def load_csv(filename):
    """Carga un archivo CSV y devuelve un DataFrame."""
    try:
        dataset = pd.read_csv(filename)
        print(f"Cargando dataset de dimensiones {dataset.shape}")
        print("Datos cargados con éxito.")
        return dataset
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None
