class Character:
    """Class representing a character in the Game of Thrones universe."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
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

    def die(self) -> None:
        """Mark the character as dead."""
        self.is_alive = False


class Stark(Character):
    """Class representing a character from the Stark family."""

    def die(self) -> None:
        """Mark the Stark character as dead."""
        super().die()  # Call the base class method


def main():
    """
    Main function to demonstrate the usage of Character and Stark classes.
    """
    try:
        # Create and test a Character instance
        ned = Character("Ned")
        print(f"Character: {ned.first_name}, Alive: {ned.is_alive}")
        ned.die()
        print(f"After die(): {ned.first_name}, Alive: {ned.is_alive}")

        # Create and test a Stark instance
        arya = Stark("Arya")
        print(f"Stark: {arya.first_name}, Alive: {arya.is_alive}")
        arya.die()
        print(f"After die(): {arya.first_name}, Alive: {arya.is_alive}")

        # Test error handling
        try:
            Character("")
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
