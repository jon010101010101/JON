"""
This module defines the Baratheon and Lannister classes,
which inherit from the Character class.
"""

from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Initialize a Baratheon character.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): Whether the character is alive.
             Defaults to True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self) -> str:
        """Return a string representation of the Baratheon character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """Return a string representation of the Baratheon character."""
        return self.__str__()

    def die(self) -> None:
        """Mark the Baratheon character as dead."""
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Initialize a Lannister character.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): Whether the character is alive.
             Defaults to True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self) -> str:
        """Return a string representation of the Lannister character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """Return a string representation of the Lannister character."""
        return self.__str__()

    def die(self) -> None:
        """Mark the Lannister character as dead."""
        self.is_alive = False

    @classmethod
    def create_lannister(
        cls,
        first_name: str,
        is_alive: bool = True
    ) -> 'Lannister':
        """
        Create and return a new Lannister character.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): Whether the character is
             alive. Defaults to True.

        Returns:
            Lannister: A new Lannister character.
        """
        return cls(first_name, is_alive)


def main():
    """
    Main function to test the Baratheon and Lannister classes.
    """
    try:
        # Test Baratheon
        robert = Baratheon("Robert")
        print(robert)
        robert.die()
        print(f"Is Robert alive? {robert.is_alive}")

        # Test Lannister
        cersei = Lannister.create_lannister("Cersei")
        print(cersei)
        cersei.die()
        print(f"Is Cersei alive? {cersei.is_alive}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
