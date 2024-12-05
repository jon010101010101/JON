"""
Este módulo define una clase calculadora para operaciones vectoriales.
"""
"""
    Una clase para realizar operaciones escalares en vectores.

    Esta clase permite la adición, multiplicación, sustracción
    y división de un escalar con cada elemento de un vector.

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
    Clase para realizar operaciones escalares en vectores.

    Esta clase permite la adición, multiplicación, sustracción
    y división de un escalar con cada elemento de un vector.
    """

    def __init__(self, vector):
        """
        Inicializa la calculadora con un vector.

        Args:
            vector (list): El vector de entrada.

        Raises:
            TypeError: Si la entrada no es una lista.
            ValueError: Si la lista está vacía o contiene valores no numéricos.
        """
        # Verifica que el vector sea una lista
        if not isinstance(vector, list):
            raise TypeError("Input must be a list")
        
        # Verifica que el vector no esté vacío
        if not vector:
            raise ValueError("Vector cannot be empty")
        
        # Verifica que todos los elementos sean numéricos (int o float)
        if not all(isinstance(x, (int, float)) for x in vector):
            raise ValueError("All elements must be numeric")

        # Asigna el vector a un atributo de instancia
        self.vector = vector

        # es un método especial de la clase calculator que permite sobrecargar el
        # operador de suma (+) para objetos de una clase personalizada
    def __add__(self, object) -> None:
        """
        Suma un escalar a cada elemento del vector.

        Args:
            object (float): El valor a sumar.

        Raises:
            TypeError: Si el objeto no es un número.
        """
        # Verifica que el objeto sea un número (int o float)
        if not isinstance(object, (int, float)):
            raise TypeError("Scalar must be a number")

        # Este es un uso de lista por comprensión, que crea una nueva lista
        #  donde cada elemento del vector original (self.vector) se incrementa
        #  por el valor del escalar (object).
        # Se itera sobre cada elemento x en el vector original, se suma
        #  el escalar object y el resultado es una nueva lista que reemplaza
        #  al al atributo self.vector
        """# Supongamos que tenemos una instancia de la clase calculator
        calc = calculator([1, 2, 3])  # Creamos una calculadora con un vector [1, 2, 3]

        # Llamamos al método __add__ usando el operador +
        calc + 5  # Esto sumará 5 a cada elemento del vector

        # La salida será: [6, 7, 8]
        """
        self.vector = [x + object for x in self.vector]
        
        # Imprime el nuevo vector
        print(self.vector)

    def __mul__(self, object) -> None:
        """
        Multiplica cada elemento del vector por un escalar.

        Args:
            object (float): El valor por el cual multiplicar.

        Raises:
            TypeError: Si el objeto no es un número.
        """
        # Verifica que el objeto sea un número (int o float)
        if not isinstance(object, (int, float)):
            raise TypeError("Scalar must be a number")

        # Multiplica cada elemento del vector por el escalar
        self.vector = [x * object for x in self.vector]
        
        # Imprime el nuevo vector
        print(self.vector)

    def __sub__(self, object) -> None:
        """
        Resta un escalar de cada elemento del vector.

        Args:
            object (float): El valor a restar.

        Raises:
            TypeError: Si el objeto no es un número.
        """
        # Verifica que el objeto sea un número (int o float)
        if not isinstance(object, (int, float)):
            raise TypeError("Scalar must be a number")

        # Resta el escalar de cada elemento del vector
        self.vector = [x - object for x in self.vector]
        
        # Imprime el nuevo vector
        print(self.vector)

    def __truediv__(self, object) -> None:
        """
        Divide cada elemento del vector por un escalar.

        Args:
            object (float): El valor por el cual dividir.

        Raises:
            TypeError: Si el objeto no es un número.
            ZeroDivisionError: Si el objeto es cero.
        """
        # Verifica que el objeto sea un número (int o float)
        if not isinstance(object, (int, float)):
            raise TypeError("Scalar must be a number")

        # Verifica que no se intente dividir por cero
        if object == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        # Divide cada elemento del vector por el escalar
        self.vector = [x / object for x in self.vector]
        
        # Imprime el nuevo vector
        print(self.vector)


if __name__ == "__main__":
    pass  # Este bloque se ejecutará si se ejecuta este archivo directamente
