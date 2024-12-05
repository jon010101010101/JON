from load_csv import load
import matplotlib.pyplot as plt


def population_dataconvert(pop_str):
    """
   Convert the population_data string into
    a numeric value in standard form.

    Args:
        pop_str (str): Population string with
        the 'M' suffix for million or  'K' for thousands

    Returns:
        float: Numeric population value.
    """
    if pop_str.endswith("M"):
        return float(pop_str[:-1]) * 1e6
    elif pop_str.endswith("k"):
        return float(pop_str[:-1]) * 1e3
    else:
        return float(pop_str)


def main():
    """
    Loads population data from a CSV file, processes and
    plots(used for creating line plots)
    the population comparison of three countries.
    """
    df = load("population_total.csv")

    country1 = "Spain"
    country2 = "France"
    country3 = "Portugal"

    spain_df = df[df['country'] == country1].iloc[:, 1:]
    france_df = df[df['country'] == country2].iloc[:, 1:]
    portugal_df = df[df['country'] == country3].iloc[:, 1:]

    spain_pop = spain_df.values.flatten()
    france_pop = france_df.values.flatten()
    portugal_pop = portugal_df.values.flatten()

    years = spain_df.columns.astype(int)

    spain_pop = [population_dataconvert(pop) for pop in spain_pop]
    france_pop = [population_dataconvert(pop) for pop in france_pop]
    portugal_pop = [population_dataconvert(pop) for pop in portugal_pop]

    plt.plot(years, spain_pop, label=country1, color='purple')
    plt.plot(years, france_pop, label=country2, color='pink')
    plt.plot(years, portugal_pop, label=country3, color='orange')

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.xticks(range(1800, 2041, 40))
    plt.xlim(1790, 2060)
    plt.ylabel("Population")

    max_pop = max(max(spain_pop), max(france_pop), max(portugal_pop))

    y_ticks = [i * 20e6 for i in range(int(max_pop / 20e6) + 1)]
    y_ticks.remove(0)
    plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])

    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
