"""
This module defines a calculator class for vector operations.
"""
"""
Code Explanation:

__init__: Initializes the object with a vector.
__add__: Adds a scalar to each element of the vector and prints it.
__mul__: Multiplies each element of the vector by a scalar and prints it.
__sub__: Subtracts a scalar from each element of the vector and prints it.
__truediv__: Divides each element of the vector by a scalar, handling
division by zero.
"""


class calculator:
    """
    A class for performing scalar operations on vectors.

    This class allows addition, multiplication, subtraction,
    and division of a scalar with each element of a vector.
    """

    def __init__(self, vector):
        """
        Initialize the calculator with a vector.

        Args:
            vector (list): The input vector.

        Raises:
            TypeError: If the input is not a list.
            ValueError: If the list is empty or contains non-numeric values.
        """
        if not isinstance(vector, list):
            raise TypeError("Input must be a list")
        if not vector:
            raise ValueError("Vector cannot be empty")
        if not all(isinstance(x, (int, float)) for x in vector):
            raise ValueError("All elements must be numeric")

        self.vector = vector

    def __add__(self, object) -> None:
        """
        Add a scalar to each element of the vector.

        Args:
            object (float): The value to add.

        Raises:
            TypeError: If the object is not a number.
        """
        if not isinstance(object, (int, float)):
            raise TypeError("Scalar must be a number")

        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """
        Multiply each element of the vector by a scalar.

        Args:
            object (float): The value to multiply by.

        Raises:
            TypeError: If the object is not a number.
        """
        if not isinstance(object, (int, float)):
            raise TypeError("Scalar must be a number")

        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """
        Subtract a scalar from each element of the vector.

        Args:
            object (float): The value to subtract.

        Raises:
            TypeError: If the object is not a number.
        """
        if not isinstance(object, (int, float)):
            raise TypeError("Scalar must be a number")

        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """
        Divide each element of the vector by a scalar.

        Args:
            object (float): The value to divide by.

        Raises:
            TypeError: If the object is not a number.
            ZeroDivisionError: If the object is zero.
        """
        if not isinstance(object, (int, float)):
            raise TypeError("Scalar must be a number")

        if object == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        self.vector = [x / object for x in self.vector]
        print(self.vector)


if __name__ == "__main__":
    pass
