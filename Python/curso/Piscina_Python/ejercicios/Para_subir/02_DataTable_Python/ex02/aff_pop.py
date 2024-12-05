import matplotlib.pyplot as plt
from load_csv import load


def convert_population(value):
    """Converts population values to float numbers."""
    if isinstance(value, str):
        if 'M' in value:
            return float(value.replace('M', '')) * 1e6
        elif 'k' in value:
            return float(value.replace('k', '')) * 1e3
    return float(value)


def display_country_info(dataset, countries, show_grid=True):
    """
    Displays population information for the specified countries.

    Args:
    dataset (pd.DataFrame): DataFrame with population data.
    countries (list): List of countries to display.
    show_grid (bool): If True, shows the grid on the graph.
    """
    plt.figure(figsize=(6, 5))
    colors = ['red', 'green', 'Blue']

    for i, country in enumerate(countries):
        if country not in dataset['country'].values:
            print(f"Error: {country} is not found in the dataset.")
            continue

        country_data = dataset[dataset['country'] == country].iloc[0, 1:]
        years = country_data.index.astype(int)
        population = country_data.apply(convert_population)

        # Filter data from 1800 to 2050
        mask = (years >= 1800) & (years <= 2050)
        plt.plot(years[mask], population[mask], label=country, color=colors[i])

    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.ylabel('Population')

    # Place the legend in the lower right corner
    plt.legend(loc='lower right')

    # Configure the x-axis to go from 1790 to 2060
    plt.xlim(1790, 2060)
    plt.xticks(range(1800, 2061, 40), rotation=0)

    # Configure the y-axis with specific values
    y_ticks = [20e6, 40e6, 60e6]
    plt.yticks(y_ticks, ['20M', '40M', '60M'])
    plt.ylim(1e6, 70e6)  # Adjust the y-axis limits

    # Show or hide the grid according to the show_grid parameter
    if show_grid:
        plt.grid(True, which="both", ls="-", alpha=0.2)

    plt.tight_layout()
    plt.show()


def main():
    # Load the dataset using the load function
    dataset = load('population_total.csv')

    if dataset is not None:
        campus_country = 'Spain'
        other_country = 'Italy'
        additional_country = 'France'

        display_country_info(
            dataset,
            [campus_country, other_country, additional_country],
            show_grid=False
        )


if __name__ == "__main__":
    main()
