import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine:
    """Represents a hot beverage vending machine."""

    class EmptyCup(HotBeverage):
        """Represents an empty cup, inheriting from HotBeverage."""

        def __init__(self):
            """Initialize the empty cup with name and price."""
            self.name = "empty cup"
            self.price = 0.90

        def description(self):
            """Return the description of the empty cup."""
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        """Custom exception for a broken coffee machine."""

        def __init__(self):
            """Initialize the exception with an error message."""
            super().__init__("This coffee machine has to be repaired.")

    def __init__(self):
        """Initialize the coffee machine with a drink counter."""
        self.served_drinks = 0

    def repair(self):
        """Reset the drink counter to repair the machine."""
        self.served_drinks = 0

    def serve(self, beverage_class):
        """
        Serve a beverage, alternating between the requested drink and an empty cup.

        Args:
            beverage_class: A class derived from HotBeverage.

        Returns:
            An instance of the requested beverage or an EmptyCup.

        Raises:
            BrokenMachineException: If the machine has served 10 or more drinks.
        """
        if self.served_drinks >= 10:
            raise self.BrokenMachineException()
        
        self.served_drinks += 1
        return random.choices([beverage_class(), self.EmptyCup()], weights=[0.75, 0.25])[0]

if __name__ == "__main__":
    # Create a coffee machine instance
    machine = CoffeeMachine()
    
    # List of beverage classes to test
    beverages = [Coffee, Tea, Chocolate, Cappuccino, HotBeverage]

    # Initialize statistics and counters
    stats = {"empty cup": 0, "coffee": 0, "tea": 0, "chocolate": 0, "cappuccino": 0, "hot beverage": 0}
    total_served = 0
    max_served = 15
    repairs = 0

    # Test loop with a drink limit
    while total_served < max_served:
        beverage = random.choice(beverages)
        try:
            served = machine.serve(beverage)
            print(f"Served: {served}")
            print()
            stats[served.name] += 1
            total_served += 1
        except machine.BrokenMachineException as e:
            print(f"Error: {e}")
            print("Repairing the machine...")
            machine.repair()
            repairs += 1
            print("Machine repaired. Continuing...")
            print()

    # Print test summary
    print("\nTest finished.")
    print(f"Total drinks served: {total_served}")
    print(f"Number of repairs: {repairs}")
    print("\nStatistics:")
    for key, value in stats.items():
        print(f"{key}: served {value} times")
