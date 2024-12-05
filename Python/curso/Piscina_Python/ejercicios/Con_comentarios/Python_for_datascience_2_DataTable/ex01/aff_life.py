import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load_csv


def display_country_info(dataset, country, show_grid=False):
    # dataset. El DataFrame que contiene los datos de esperanza de vida.
    # show_grid: Un booleano que determina si se debe mostrar una cuadrícula
    #  en el gráfico (por defecto es False).
    """Displays information for a country and plots the life expectancy."""
    print(f"Searching for data for the country: {country}")

    # Si 'country' es una columna, filtra el conjunto de datos para obtener
    # las filas donde la columna 'country' coincide con el país especificado.
    # Si 'country' no es una columna, asume que los países están en el índice
    #  y trata de localizar los datos del país usando loc. Si el país no se 
    # encuentra en el índice, crea un DataFrame vacío.
    if 'country' in dataset.columns:
        country_data = dataset[dataset['country'] == country]
    else:
        country_data = (dataset.loc[country]
                        if country in dataset.index else pd.DataFrame())

    # Si no se encuentran datos para el país (resultando en un DataFrame vacío),
    # imprime un mensaje que dice "No se encontraron datos para el país" y sale
    #  de la función.
    if country_data.empty:
        print(f"No se encontraron datos para el país: {country}")
        return

    print(f"Datos encontrados:\n{country_data}")

    # verifica si es de una serie panda
    if isinstance(country_data, pd.Series):
        #assume que el indice de la serie contiene años y los convierte
        #  en enteros
        years = country_data.index.astype(int)
        # Toma los vaores como esperanza de vida
        life_expectancy = country_data.values
    else: # si contry_data no es una serie
        # Toma todas las columnas excepto la primera (asumiendo que la 
        # primera es el nombre del país) y las convierte a enteros. Esto
        # asume que las columnas representan años.
        years = country_data.columns[1:].astype(int)
        # Selecciona la primera fila (índice 0) y todas las columnas excepto
        #  la primera, y toma estos valores como los datos de esperanza de vida.
        life_expectancy = country_data.iloc[0, 1:].values

    plt.figure(figsize=(6, 5))
    # marker='o'que los marcadores sean circulares
    # markersize=0, tamaño de los marcadores
    # linewidth=1.2: Define el grosor de la línea.
    plt.plot(years, life_expectancy, marker='o', markersize=0,
             linewidth=1.2, color='red')

    plt.title(f"Proyecciones de Expectativa de Vida de {country}")
    plt.xlabel("Año")
    plt.ylabel("Expectativa de Vida")

    plt.xticks(range(1800, 2101, 40), rotation=0)
    plt.grid(show_grid)
    # plt.tight_layout() es una herramienta valiosa para mejorar automáticamente
    #  la disposición de los elementos en una figura de Matplotlib
    plt.tight_layout()
    plt.show()


def main():
    # Cargar el conjunto de datos
    dataset = load_csv('life_expectancy_years.csv')
    if dataset is not None:
        print(dataset.head())  # Mostrar las primeras filas
        print(dataset.columns)  # Mostrar las columnas
        print(dataset.index)  # Mostrar el índice

        campus_country = 'Spain'
        mostrar_info_pais(dataset, campus_country)


if __name__ == "__main__":
    main()
