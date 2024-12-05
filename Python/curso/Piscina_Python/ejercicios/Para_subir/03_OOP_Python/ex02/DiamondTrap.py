"""
This module defines the King class, inheriting from Baratheon and Lannister.
"""

from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Represents a King character, inheriting traits from Baratheon and
    Lannister.

    This class allows for the creation of a King with specific physical
    traits and the ability to modify these traits.
    """

    def __init__(self, first_name: str) -> None:
        """
        Initialize a King instance.

        Args:
            first_name (str): The first name of the King.
        """
        super().__init__(first_name)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def set_eyes(self, color: str) -> None:
        """
        Set the eye color of the King.

        Args:
            color (str): The new eye color.
        """
        self.eyes = color

    def set_hairs(self, color: str) -> None:
        """
        Set the hair color of the King.

        Args:
            color (str): The new hair color.
        """
        self.hairs = color

    def get_eyes(self) -> str:
        """
        Get the current eye color of the King.

        Returns:
            str: The current eye color.
        """
        return self.eyes

    def get_hairs(self) -> str:
        """
        Get the current hair color of the King.

        Returns:
            str: The current hair color.
        """
        return self.hairs


def main():
    """
    Main function to test the King class.
    """
    try:
        # Create a King instance
        robert = King("Robert")

        # Display initial attributes
        print(
            f"King: {robert.first_name}, "
            f"Family: {robert.family_name}, "
            f"Eyes: {robert.get_eyes()}, "
            f"Hair: {robert.get_hairs()}"
        )

        # Modify attributes
        robert.set_eyes("green")
        robert.set_hairs("black")

        # Display modified attributes
        print(
            f"Modified King: {robert.first_name}, "
            f"Family: {robert.family_name}, "
            f"Eyes: {robert.get_eyes()}, "
            f"Hair: {robert.get_hairs()}"
        )

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
