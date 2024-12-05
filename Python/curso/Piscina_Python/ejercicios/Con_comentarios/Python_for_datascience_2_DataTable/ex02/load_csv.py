import pandas as pd


def cargar(nombre_archivo):
    """Carga el archivo CSV y devuelve un DataFrame."""
    try:
        # Intenta leer el archivo CSV
        datos = pd.read_csv(nombre_archivo)
        
        # Si la carga es exitosa, imprime un mensaje y las primeras filas
        print("Datos cargados exitosamente:")
        print(datos.head())
        
        # Devuelve el DataFrame
        return datos
    except Exception as e:
        # Si ocurre un error, imprime el mensaje de error
        print(f"Error al cargar el archivo: {e}")
        
        # Devuelve None en caso de error
        return None

