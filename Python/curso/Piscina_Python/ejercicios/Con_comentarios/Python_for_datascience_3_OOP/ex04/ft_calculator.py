"""
This module defines a calculator class for vector operations.
"""


class calculator:
    """
    A calculator class for performing operations on vectors.

    Esta clase proporciona métodos estáticos para calcular el producto punto,
    la suma y la resta de dos vectores.
    """

    # decorador
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculates and displays the dot product of two vectors.

        Calcula y muestra el producto punto de dos vectores.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.

        Returns:
            None: Prints the result of the dot product.

        Raises:
            TypeError: If inputs are not lists or contain non-numeric values.
            ValueError: If vectors have different lengths.
        """
        # Verifica si ambos inputs son listas
        if not (isinstance(V1, list) and isinstance(V2, list)):
            raise TypeError("Both inputs must be lists")
        # Verifica si los vectores tienen la misma longitud
        if len(V1) != len(V2):
            raise ValueError("Vectors must have the same length")
        try:
            # Calcula el producto punto utilizando la función zip para emparejar
            #  elementos
            # La función zip toma dos o más iterables (en este caso, las listas 
            # V1 y V2) y devuelve un iterador que genera tuplas. Cada tupla 
            # contiene elementos emparejados de los iterables.
            # Por ejemplo, si V1 = [1, 2, 3] y V2 = [4, 5, 6], entonces 
            # zip(V1, V2) generará: [(1, 4), (2, 5), (3, 6)].
            # La expresión float(x) * float(y) for x, y in zip(V1, V2) es una 
            # comprensión de generador que itera sobre cada par de elementos 
            # (x, y) producidos por zip.
            result = sum(float(x) * float(y) for x, y in zip(V1, V2))
            # Imprime el resultado del producto punto
            print(f"Dot product is: {int(result)}")
        except ValueError:
            raise TypeError("All elements must be numeric")
    
    # decorador
    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Calculates and displays the sum of two vectors.

        Calcula y muestra la suma de dos vectores.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.

        Returns:
            None: Prints the resulting vector from the addition.

        Raises:
            TypeError: If inputs are not lists or contain non-numeric values.
            ValueError: If vectors have different lengths.
        """
        # Verifica si ambos inputs son listas
        if not (isinstance(V1, list) and isinstance(V2, list)):
            raise TypeError("Both inputs must be lists")
        # Verifica si los vectores tienen la misma longitud
        if len(V1) != len(V2):
            raise ValueError("Vectors must have the same length")
        try:
            # Suma los elementos correspondientes de los vectores
            result = [float(x) + float(y) for x, y in zip(V1, V2)]
            # Imprime el vector resultante de la suma
            print(f"Add Vector is : {[round(num, 1) for num in result]}")
        except ValueError:
            raise TypeError("All elements must be numeric")

    # decorador
    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Calculates and displays the subtraction of two vectors.

        Calcula y muestra la resta de dos vectores.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.

        Returns:
            None: Prints the resulting vector from the subtraction.

        Raises:
            TypeError: If inputs are not lists or contain non-numeric values.
            ValueError: If vectors have different lengths.
        """
        # Verifica si ambos inputs son listas
        if not (isinstance(V1, list) and isinstance(V2, list)):
            raise TypeError("Both inputs must be lists")
        # Verifica si los vectores tienen la misma longitud
        if len(V1) != len(V2):
            raise ValueError("Vectors must have the same length")
        try:
            # Resta los elementos correspondientes de los vectores
            result = [float(x) - float(y) for x, y in zip(V1, V2)]
            # Imprime el vector resultante de la resta
            print(f"Sous Vector is: {[round(num, 1) for num in result]}")
        except ValueError:
            raise TypeError("All elements must be numeric")


if __name__ == "__main__":
    pass  # Este bloque se ejecuta si se ejecuta este archivo directamente.

"""
    def dotproduct(V1, V2):
    # Supongamos que ya se han realizado las validaciones necesarias
    result = sum(float(x) * float(y) for x, y in zip(V1, V2))
    print(f"Dot product is: {int(result)}")

    # Ejemplo de uso
    dotproduct([1, 2, 3], [4, 5, 6])

    Ejemplo de Entrada: Si llamamos a dotproduct([1, 2, 3], [4, 5, 6]), 
    el cálculo del producto punto sería:
        (1×4)+(2×5)+(3×6)=4+10+18=32
       imprimira Dot product is: 32
    """
"""
Definición de los Vectores

    Vector A=[1,2,3]
    Vector B=[4,5,6]

Suma de Vectores
Para sumar estos dos vectores, simplemente sumamos sus componentes correspondientes. La operación se realiza de la siguiente manera:
A+B=[1+4,2+5,3+6]
Cálculo Paso a Paso

    Suma de la primera componente:
        1+4=5
    Suma de la segunda componente:
        2+5=7
    Suma de la tercera componente:
        3+6=9

Resultado Final
Por lo tanto, la suma de los vectores es:
A+B=[5,7,9]
A+B=[5,7,9]

""" 
"""
Definición de los Vectores

    Vector A=[1,2,3]
    Vector B=[4,5,6]

Resta de Vectores
Para restar estos dos vectores, simplemente restamos sus componentes correspondientes. La operación se realiza de la siguiente manera:
A−B=[1−4,2−5,3−6]

Cálculo Paso a Paso

    Resta de la primera componente:
        1−4=−3
    Resta de la segunda componente:
        2−5=−3
    Resta de la tercera componente:
        3−6=−3

Resultado Final
Por lo tanto, la resta de los vectores es:
A−B=[−3,−3,−3]

"""