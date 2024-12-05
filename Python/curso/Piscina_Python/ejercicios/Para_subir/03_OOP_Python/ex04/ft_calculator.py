"""
This module defines a calculator class for vector operations.
"""


class calculator:
    """
    A calculator class for performing operations on vectors.

    This class provides static methods to calculate the dot product,
    addition, and subtraction of two vectors.
    """

    # decorator
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculates and displays the dot product of two vectors.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.

        Returns:
            None: Prints the result of the dot product.

        Raises:
            TypeError: If inputs are not lists or contain non-numeric values.
            ValueError: If vectors have different lengths.
        """
        if not (isinstance(V1, list) and isinstance(V2, list)):
            raise TypeError("Both inputs must be lists")
        if len(V1) != len(V2):
            raise ValueError("Vectors must have the same length")
        try:
            result = sum(float(x) * float(y) for x, y in zip(V1, V2))
            print(f"Dot product is: {int(result)}")
        except ValueError:
            raise TypeError("All elements must be numeric")

    # decorator
    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Calculates and displays the sum of two vectors.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.

        Returns:
            None: Prints the resulting vector from the addition.

        Raises:
            TypeError: If inputs are not lists or contain non-numeric values.
            ValueError: If vectors have different lengths.
        """
        if not (isinstance(V1, list) and isinstance(V2, list)):
            raise TypeError("Both inputs must be lists")
        if len(V1) != len(V2):
            raise ValueError("Vectors must have the same length")
        try:
            result = [float(x) + float(y) for x, y in zip(V1, V2)]
            print(f"Add Vector is : {[round(num, 1) for num in result]}")
        except ValueError:
            raise TypeError("All elements must be numeric")

    # decorator
    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Calculates and displays the subtraction of two vectors.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.

        Returns:
            None: Prints the resulting vector from the subtraction.

        Raises:
            TypeError: If inputs are not lists or contain non-numeric values.
            ValueError: If vectors have different lengths.
        """
        if not (isinstance(V1, list) and isinstance(V2, list)):
            raise TypeError("Both inputs must be lists")
        if len(V1) != len(V2):
            raise ValueError("Vectors must have the same length")
        try:
            result = [float(x) - float(y) for x, y in zip(V1, V2)]
            print(f"Sous Vector is: {[round(num, 1) for num in result]}")
        except ValueError:
            raise TypeError("All elements must be numeric")


if __name__ == "__main__":
    pass
