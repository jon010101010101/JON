from abc import ABC, abstractmethod


class Character(ABC):
    """An Abstract Base class representing a Character"""

    def __init__(self, first_name, is_alive=True):
        """Initilise a character with a name and an optional is_alive"""
        super().__init__()
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Method to change the health state of the character.
        This method should be implemented by subclasses."""
        pass


class Stark(Character):
    """A  Character part of the Stark Family"""

    def die(self):
        """Dead the Stark"""
        self.is_alive = False
