from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive=True) -> None:
        """
        Initialise a Baratheon
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self) -> str:
        '''String representation'''
        return super().__str__()

    def __repr__(self) -> str:
        '''Representation'''
        repr = tuple([y for x, y in self.__dict__.items() if
                      x not in ["is_alive", "first_name"]])
        return "Vector: " + str(repr)

    def die(self) -> None:
        """Dead the Baratheon"""
        self.is_alive = False


class Lannister(Character):
    """A Character part of the Lannister Family"""

    def __init__(self, first_name: str, is_alive=True) -> None:
        """Initialise a Lannister"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self) -> str:
        '''String representation'''
        return super().__str__()

    def __repr__(self) -> str:
        '''Representation'''
        repr = tuple([y for x, y in self.__dict__.items() if
                      x not in ["is_alive", "first_name"]])
        return "Vector: " + str(repr)

    def die(self) -> None:
        """Dead the Lannister"""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name: str, is_alive=True) -> None:
        """
        Create a Lannister character instance with custom is_alive status.
        Returns:
            Lannister: An instance of the Lannister character.
        """
        instance = cls(first_name, is_alive=is_alive)
        return instance
