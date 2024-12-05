from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Carga datos del Producto Nacional Bruto (PNB) per cápita
    y la esperanza de vida desde archivos CSV separados.
    Se enfoca en los datos del año 1900 y visualiza la correlación
    entre el PNB y la esperanza de vida a través de un gráfico de dispersión.
    """
    # Cargar datos de ingresos y esperanza de vida
    income_data = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    )
    life_expectancy_data = load("life_expectancy_years.csv")

    # Definir la columna para el año 1900
    year_1900_column = '1900'

    # Acceder a los datos de PNB y esperanza de vida para el año 1900
    gnp_1900 = income_data[year_1900_column]
    life_expectancy_1900 = life_expectancy_data[year_1900_column]

    # Crear un gráfico de dispersión
    plt.figure(figsize=(6, 5))  # Establecer el tamaño de la figura
    plt.scatter(gnp_1900, life_expectancy_1900)  # Graficar los puntos
    plt.title("1900")  # Título del gráfico
    plt.xlabel("Producto Nacional Bruto")  # Etiqueta para el eje x
    plt.ylabel("Esperanza de Vida")  # Etiqueta para el eje y

    # Establecer el eje x en escala logarítmica para mejor visualización
    plt.xscale("log")
    plt.xticks(
        ticks=[300, 1000, 10000],
        labels=['300', '1k', '10k']
    )  # Personalizar las marcas del eje x

    plt.tight_layout()  # Ajustar el diseño para evitar superposiciones
    plt.show()  # Mostrar el gráfico


if __name__ == "__main__":
    main()  # Ejecutar la función main si este archivo se ejecuta directamente

