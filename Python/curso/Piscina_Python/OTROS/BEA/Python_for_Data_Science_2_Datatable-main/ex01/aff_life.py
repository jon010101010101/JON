from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Load life expectancy data, filter for Spain, and display a line graph.

    Loads the life expectancy dataset from a CSV file, filters the data for
    Spain, and displays a line graph showing the life expectancy in Spain
    over the years. The x-axis of the graph includes year labels from
    1800 to 2080, with every 40th year label displayed and rotated for clarity.
    The graph includes a title, axis labels, legend, and grid.
    """
    df = load("life_expectancy_years.csv")

    spain_data = df[df['country'] == 'Spain']

    years = spain_data.columns[1:]
    life_expectancy = spain_data.values[0][1:]

    plt.plot(years, life_expectancy)
    plt.title('Spain Life expectancy Projections')
    plt.xlabel('Year')
    plt.xticks(years[::40])
    plt.ylabel('Life expectancy')
    plt.yticks(range(30, 100, 10))
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
