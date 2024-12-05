import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    """
    Carga un DataFrame CSV desde la ruta especificada y lo devuelve
    como un DataFrame de pandas.

    Parámetros:
    path (str): La ruta al archivo CSV que se va a cargar.

    Retorna:
    pd.DataFrame: El DataFrame cargado como un DataFrame de pandas.

    Si hay un error (por ejemplo, ruta incorrecta, formato incorrecto)
    , imprime el mensaje de error y devuelve None.
    """
    try:
        # Comprobar si el formato del archivo es .csv
        # path(ruta) lower (minusculas) endswith ( verrifica si termina en csv)
        if not path.lower().endswith('.csv'):
            raise ValueError("El formato del archivo no es .csv.")

        # Comprobar si el archivo existe
        if not os.path.exists(path):
            raise FileNotFoundError("La ruta es incorrecta.")

        # Cargar el CSV sin establecer el índice primero para verificar las
        #  columnas
        # pd.read_csv, biblioteca de panda para leeer archivos CSV
        # df (DataFrame) variable donde se almacenara
        df = pd.read_csv(path)

        # Imprimir las dimensiones del conjunto de datos cargado
        # df.shape atributo del df devulve una tupla el primer elemento
        # es el nª filas y el 2ª columnas
        print(f"Cargando conjunto de datos de dimensiones {df.shape}")

        # Cargar el CSV y establecer el país como índice
        df = pd.read_csv(path, index_col="country")
        return df

    except (FileNotFoundError, ValueError) as error:
        print(type(error).__name__ + ":", error)
        return None
