"""
This module defines a calculator class for vector operations.
"""
"""
Explicación del Código:

__init__: Inicializa el objeto con un vector.
__add__: Suma un escalar a cada elemento del vector y lo imprime.
__mul__: Multiplica cada elemento del vector por un escalar y lo imprime.
__sub__: Resta un escalar de cada elemento del vector y lo imprime.
__truediv__: Divide cada elemento del vector por un escalar, manejando
la división por cero.
"""


class calculator:
    """
    A class for performing scalar operations on vectors.

    Esta clase permite la adición, multiplicación, sustracción,
    y división de un escalar con cada elemento de un vector.
    """

    def __init__(self, vector):
        """
        Initialize the calculator with a vector.

        Inicializa la calculadora con un vector.

        Args:
            vector (list): The input vector.

        Raises:
            TypeError: If the input is not a list.
            ValueError: If the list is empty or contains non-numeric values.
        """
        # Verifica si el input es una lista
        if not isinstance(vector, list):
            raise TypeError("Input must be a list")
        # Verifica si la lista no está vacía
        if not vector:
            raise ValueError("Vector cannot be empty")
        # Verifica si todos los elementos son numéricos
        if not all(isinstance(x, (int, float)) for x in vector):
            raise ValueError("All elements must be numeric")

        # Asigna el vector a la instancia
        self.vector = vector

    def __add__(self, object) -> None:
        """
        Add a scalar to each element of the vector.

        Suma un escalar a cada elemento del vector.

        Args:
            object (float): The value to add.

        Raises:
            TypeError: If the object is not a number.
        """
        # Verifica si el objeto es un número
        if not isinstance(object, (int, float)):
            raise TypeError("Scalar must be a number")

        # Suma el escalar a cada elemento del vector y actualiza el vector
        # La expresión [x + object for x in self.vector] es una list comprehension
        #  en Python, que es una forma concisa y eficiente de crear listas.
        # En este caso, se está creando una nueva lista que contiene los resultados
        #  de sumar un escalar (denominado object) a cada elemento del vector 
        # original (self.vector).
        # for x in self.vector: Esto significa que se está iterando sobre cada 
        # elemento x en self.vector
        # self.vector es el atributo de la instancia que contiene la lista original
        #  de números (el vector)
        self.vector = [x + object for x in self.vector]
        # Imprime el nuevo vector
        print(self.vector)

    def __mul__(self, object) -> None:
        """
        Multiply each element of the vector by a scalar.

        Multiplica cada elemento del vector por un escalar.

        Args:
            object (float): The value to multiply by.

        Raises:
            TypeError: If the object is not a number.
        """
        # Verifica si el objeto es un número
        if not isinstance(object, (int, float)):
            raise TypeError("Scalar must be a number")

        # Multiplica el escalar por cada elemento del vector y actualiza el vector
        self.vector = [x * object for x in self.vector]
        # Imprime el nuevo vector
        print(self.vector)

    def __sub__(self, object) -> None:
        """
        Subtract a scalar from each element of the vector.

        Resta un escalar de cada elemento del vector.

        Args:
            object (float): The value to subtract.

        Raises:
            TypeError: If the object is not a number.
        """
        # Verifica si el objeto es un número
        if not isinstance(object, (int, float)):
            raise TypeError("Scalar must be a number")

        # Resta el escalar de cada elemento del vector y actualiza el vector
        self.vector = [x - object for x in self.vector]
        # Imprime el nuevo vector
        print(self.vector)

    def __truediv__(self, object) -> None:
        """
        Divide each element of the vector by a scalar.

        Divide cada elemento del vector por un escalar.

        Args:
            object (float): The value to divide by.

        Raises:
            TypeError: If the object is not a number.
            ZeroDivisionError: If the object is zero.
        """
        # Verifica si el objeto es un número
        if not isinstance(object, (int, float)):
            raise TypeError("Scalar must be a number")

        # Verifica si se intenta dividir por cero
        if object == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        # Divide cada elemento del vector por el escalar y actualiza el vector
        self.vector = [x / object for x in self.vector]
        # Imprime el nuevo vector
        print(self.vector)


if __name__ == "__main__":
    pass  # Este bloque se ejecuta si se ejecuta este archivo directamente.

