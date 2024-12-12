import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load_csv

"""
This script analyzes and visualizes life expectancy data for specific
 countries.

Dependencies:
- pandas: For data manipulation and analysis.
- matplotlib: For creating visualizations.
- load_csv: Custom module for loading CSV data.
"""


def display_country_info(dataset, country, show_grid=False):
    """
    Displays information for a country and plots its life expectancy over time.

    Args:
    dataset (pd.DataFrame): DataFrame containing life expectancy data.
    country (str): Name of the country to analyze.
    show_grid (bool): If True, displays a grid on the plot. Default is False.

    Returns:
    None: The function prints information and displays a plot.
    """
    print(f"Searching for data for the country: {country}")

    # Extract country data based on dataset structure
    if 'country' in dataset.columns:
        country_data = dataset[dataset['country'] == country]
    else:
        country_data = (dataset.loc[country]
                        if country in dataset.index else pd.DataFrame())

    if country_data.empty:
        print(f"No data found for the country: {country}")
        return

    print(f"Data found:\n{country_data}")

    # Prepare data for plotting
    if isinstance(country_data, pd.Series):
        years = country_data.index.astype(int)
        life_expectancy = country_data.values
    else:
        years = country_data.columns[1:].astype(int)
        life_expectancy = country_data.iloc[0, 1:].values

    # Create and configure the plot
    plt.figure(figsize=(6, 5))
    plt.plot(years, life_expectancy, marker='o', markersize=0,
             linewidth=1.2, color='red')

    plt.title(f"{country} Life Expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")

    plt.xticks(range(1800, 2101, 40), rotation=0)
    plt.grid(show_grid)

    plt.tight_layout()
    plt.show()


def main():
    """
    Main function to load the dataset and display information for a
    specific country.

    This function:
    1. Loads the 'life_expectancy_years.csv' dataset.
    2. Prints basic information about the dataset.
    3. Calls display_country_info for Spain.
    """
    dataset = load_csv('life_expectancy_years.csv')
    if dataset is not None:
        print(dataset.head())
        print(dataset.columns)
        print(dataset.index)

        campus_country = 'Spain'
        display_country_info(dataset, campus_country)


if __name__ == "__main__":
    main()
