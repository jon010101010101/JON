# Base class for hot beverages
class HotBeverage:
    """
    Represents a generic hot beverage with default attributes and methods.
    """
    price = 0.30
    name = "hot beverage"

    def description(self) -> str:
        """
        Provides a default description for hot beverages.

        Returns:
            str: Description of the hot beverage.
        """
        return "Just some hot water in a cup."

    def __str__(self) -> str:
        """
        Formats the string representation of the beverage.

        Returns:
            str: Formatted string with name, price, and description.
        """
        return (f"name : {self.name}\n"
                f"price : {self.price:.2f}\n"
                f"description : {self.description()}")


# Class for coffee, inherits from HotBeverage
class Coffee(HotBeverage):
    """
    Represents a coffee beverage with specific attributes and methods.
    """
    name = "coffee"
    price = 0.40

    def description(self) -> str:
        """
        Provides a specific description for coffee.

        Returns:
            str: Description of the coffee.
        """
        return "A coffee, to stay awake."


# Class for tea, inherits from HotBeverage
class Tea(HotBeverage):
    """
    Represents a tea beverage. Inherits default attributes and methods.
    """
    name = "tea"
    # No need to redefine price or description as they are inherited


# Class for chocolate, inherits from HotBeverage
class Chocolate(HotBeverage):
    """
    Represents a chocolate beverage with specific attributes and methods.
    """
    name = "chocolate"
    price = 0.50

    def description(self) -> str:
        """
        Provides a specific description for chocolate.

        Returns:
            str: Description of the chocolate.
        """
        return "Chocolate, sweet chocolate..."


# Class for cappuccino, inherits from HotBeverage
class Cappuccino(HotBeverage):
    """
    Represents a cappuccino beverage with specific attributes and methods.
    """
    name = "cappuccino"
    price = 0.45

    def description(self) -> str:
        """
        Provides a specific description for cappuccino.

        Returns:
            str: Description of the cappuccino.
        """
        return "Un po' di Italia nella sua tazza!"


# Tests
if __name__ == "__main__":
    # Create a list with an instance of each type of beverage
    beverages = [HotBeverage(), Coffee(), Tea(), Chocolate(), Cappuccino()]
    
    # Print the information of each beverage
    for beverage in beverages:
        print(beverage)
        print()  # Blank line to separate beverages
