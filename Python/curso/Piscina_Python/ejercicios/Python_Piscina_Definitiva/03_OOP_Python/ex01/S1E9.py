from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class representing a character in the Game of
    Thrones universe."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Your docstring for Constructor"""
        """
        Initialize a character.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): Indicates if the character is alive.
                Defaults to True.

        Raises:
            ValueError: If first_name is empty or not a string.
            TypeError: If is_alive is not a boolean.
        """
        if not isinstance(first_name, str) or not first_name:
            raise ValueError("First name must be a non-empty string.")
        if not isinstance(is_alive, bool):
            raise TypeError("is_alive must be a boolean.")

        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None:
        """
        Abstract method to mark the character as dead.
        This method must be implemented by all subclasses.
        """
        pass


class Stark(Character):
    """Your docstring for Class"""
    """Class representing a character from the Stark family."""

    def die(self) -> None:
        """Your docstring for Method"""
        """Mark the Stark character as dead."""
        self.is_alive = False


def main():
    """
    Main function to demonstrate the usage of Character and Stark classes.
    """
    try:
        # We can't create an instance of Character as it's abstract
        # ned = Character("Ned")  # This would raise an error

        # Create and test a Stark instance
        arya = Stark("Arya")
        print(f"Stark: {arya.first_name}, Alive: {arya.is_alive}")
        arya.die()
        print(f"After die(): {arya.first_name}, Alive: {arya.is_alive}")

        # Test error handling
        try:
            Stark("")
        except ValueError as e:
            print(f"Caught expected error: {e}")

        try:
            Stark("Invalid", is_alive="Not a boolean")
        except TypeError as e:
            print(f"Caught expected error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
