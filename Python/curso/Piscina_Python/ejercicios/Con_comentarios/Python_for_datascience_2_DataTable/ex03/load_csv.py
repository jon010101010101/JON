import pandas as pd


def load(nombre_archivo):
    """Carga un archivo CSV y devuelve un DataFrame."""
    try:
        # Intenta leer el archivo CSV utilizando pandas
        data = pd.read_csv(nombre_archivo)
        
        # Si la lectura es exitosa, devuelve el DataFrame
        return data
    except Exception as e:
        # Si ocurre algún error durante la carga, imprime un mensaje de error
        print(f"Error al cargar el archivo {nombre_archivo}: {e}")
        
        # En caso de error, devuelve None
        return None

