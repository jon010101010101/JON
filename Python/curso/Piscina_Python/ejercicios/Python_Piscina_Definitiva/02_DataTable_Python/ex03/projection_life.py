from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Loads data for Gross National Product (GNP) per capita
    and life expectancy from separate CSV files.
    It focuses on data from the year 1900 and visualizes the correlation
    between GNP and life expectancy through a scatter plot.
    """
    # Load income and life expectancy data
    income_data = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    )
    life_expectancy_data = load("life_expectancy_years.csv")

    # Define the column for the year 1900
    year_1900_column = '1900'

    # Access GNP and life expectancy data for the year 1900
    gnp_1900 = income_data[year_1900_column]
    life_expectancy_1900 = life_expectancy_data[year_1900_column]

    # Create a scatter plot
    plt.figure(figsize=(6, 5))  # Set the figure size
    plt.scatter(gnp_1900, life_expectancy_1900)  # Plot the points
    plt.title("1900")  # Title of the plot
    plt.xlabel("Gross National Product")  # Label for the x-axis
    plt.ylabel("Life Expectancy")  # Label for the y-axis

    # Set the x-axis to a logarithmic scale for better visualization
    plt.xscale("log")
    plt.xticks(
        ticks=[300, 1000, 10000],
        labels=['300', '1k', '10k']
    )  # Customize x-axis ticks

    plt.tight_layout()  # Adjust layout to avoid overlaps
    plt.show()  # Display the plot


if __name__ == "__main__":
    main()  # Run the main function if this file is executed directly
