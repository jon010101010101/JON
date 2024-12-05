import matplotlib.pyplot as plt
from load_csv import load


def convert_population(value):
    """Convierte valores de población a números flotantes."""
    if isinstance(value, str):
        if 'M' in value: # en millones
            return float(value.replace('M', '')) * 1e6
        elif 'k' in value: # en miles
            return float(value.replace('k', '')) * 1e3
    return float(value)


def display_country_info(dataset, countries, show_grid=True):
    """
    Muestra la información de población para los países especificados.

    Args:
    dataset (pd.DataFrame): DataFrame con los datos de población.
    countries (list): Lista de países a mostrar.
    show_grid (bool): Si True, muestra la cuadrícula en el gráfico.
    """
    plt.figure(figsize=(6, 5))
    colors = ['red', 'green', 'Blue']

    for i, country in enumerate(countries): # Itera sobre la lista contries
        #verifica si el pais actual no esta en la columna countr de dataset
        if country not in dataset['country'].values:
            print(f"Error: {country} no se encuentra en el dataset.")
            continue
        
        # filtra dataset para obtener la fila del pais
        # .iloc[0, 1:] seleccciona la primera fila del resultado y todas las
        #  columnas excpto la primera
        country_data = dataset[dataset['country'] == country].iloc[0, 1:]
        # extrae los años y los convierte en enteros
        years = country_data.index.astype(int)
        #convierte los datos de poblacion a un formato numerico constante
        population = country_data.apply(convert_population)

        # Filtrar datos de 1800 a 2050
        mask = (years >= 1800) & (years <= 2050)
        # mask es un array de la misma longitud que years y population y da true
        # cuando se quiere incluir y false excluye
        plt.plot(years[mask], population[mask], label=country, color=colors[i])

    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.ylabel('Population')

    # Colocar la leyenda en la esquina inferior derecha
    plt.legend(loc='lower right')

    # Configurar el eje x para que vaya de 1790 a 2060
    plt.xlim(1790, 2060)
    plt.xticks(range(1800, 2061, 40), rotation=45)

    # Configurar el eje y con los valores específicos
    y_ticks = [20e6, 40e6, 60e6]
    plt.yticks(y_ticks, ['20M', '40M', '60M'])
    plt.ylim(1e6, 70e6)  # Ajustar los límites del eje y

    # Mostrar u ocultar la cuadrícula según el parámetro show_grid
    # True: Activa la cuadrícula
    # which="both": Aplica la cuadrícula tanto a los ejes principales como a
    #  los secundarios.
    # ls="-": Establece el estilo de línea de la cuadrícula como una línea sólida.
    # alpha=0.2: Establece la transparencia de la cuadrícula. 0.2 significa que
    #  es bastante transparente (80% transparente).
    if show_grid:
        plt.grid(True, which="both", ls="-", alpha=0.2)

    plt.tight_layout()
    plt.show()


def main():
    # Cargar el dataset usando la función load
    dataset = load('population_total.csv')

    if dataset is not None:
        campus_country = 'Spain'
        other_country = 'Italy'
        additional_country = 'France'

        # Puedes cambiar True a False si no deseas mostrar la cuadrícula
        display_country_info(
            dataset,
            [campus_country, other_country, additional_country],
            show_grid=False
        )
    else:
        print("No se pudo cargar el dataset.")


if __name__ == "__main__":
    main()
