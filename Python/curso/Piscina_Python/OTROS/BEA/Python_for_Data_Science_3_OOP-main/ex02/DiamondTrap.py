from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """The mad King himself"""
    def __init__(self, first_name, is_alive=True):
        """Initializes the king, a cross between a Barathon and Lannister"""
        super().__init__(first_name, is_alive)

    def get_eyes(self) -> str:
        "Getter for eye color"
        return self._eyes

    def set_eyes(self, color: str) -> None:
        "Setter for eye color"
        self._eyes = color

    def get_hairs(self) -> str:
        "Getter for hair color"
        return self._hairs

    def set_hairs(self, color) -> None:
        "Setter for hair color"
        self._hairs = color

    eyes = property(get_eyes, set_eyes, doc="Proptery for eye color")
    hairs = property(get_hairs, set_hairs, doc="Proptery for hair color")
