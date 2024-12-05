"""
Este módulo define una clase calculadora para operaciones vectoriales.
"""
"""
"""
    Una clase calculadora para realizar operaciones en vectores.

    Esta clase proporciona métodos estáticos para calcular el producto punto,
    la suma y la resta de dos vectores.

    Explicación del Código:

    @staticmethod: Este decorador se utiliza para definir métodos que pueden
    ser llamados en la clase sin necesidad de instanciarla.
    dotproduct: Calcula el producto punto de dos vectores. Utiliza la función zip
    para emparejar elementos de ambos vectores y suma los productos.
    add_vec: Suma los elementos de dos vectores y devuelve el resultado como
    una lista.
    sub_vec: Resta los elementos de dos vectores y devuelve el resultado
    como una lista.
"""
"""
class calculator:
    """
    Clase calculadora para realizar operaciones en vectores.

    Esta clase proporciona métodos estáticos para calcular el producto punto,
    la suma y la resta de dos vectores.
    """

    # Decorador para definir un método estático
    # Un decorador es una función que toma otra función como argumento, realiza 
    # alguna operación sobre ella (como añadir funcionalidad) y devuelve una 
    # nueva función. Esto se hace comúnmente utilizando el símbolo @ seguido
    #  del nombre del decorador justo encima de la función que se desea decorar.
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calcula y muestra el producto punto de dos vectores.

        Args:
            V1 (list[float]): El primer vector.
            V2 (list[float]): El segundo vector.

        Returns:
            None: Imprime el resultado del producto punto.

        Raises:
            TypeError: Si las entradas no son listas o contienen valores no numéricos.
            ValueError: Si los vectores tienen diferentes longitudes.
        """
        # Verifica que ambas entradas sean listas
        if not (isinstance(V1, list) and isinstance(V2, list)):
            raise TypeError("Both inputs must be lists")
        
        # Verifica que los vectores tengan la misma longitud
        if len(V1) != len(V2):
            raise ValueError("Vectors must have the same length")
        
        try:
            # Calcula el producto punto usando una comprensión de generador
            # Uso de zip(V1, V2) zip(V1, V2) es una función incorporada de Python que 
            # toma dos o más iterables (en este caso, las listas V1 y V2) y devuelve un 
            # iterador de tuplas. Cada tupla contiene elementos emparejados de los
            #  iterables originales.
            #Por ejemplo, si V1 = [1, 2, 3] y V2 = [4, 5, 6], entonces 
            # zip(V1, V2) producirá el siguiente resultado:
            # [(1, 4), (2, 5), (3, 6)]

            # La expresión (float(x) * float(y) for x, y in zip(V1, V2)) es una 
            # comprensión de generador. Esto significa que se está creando un 
            # generador que producirá valores uno a uno en lugar de crear una 
            # lista completa en memoria.
            # Para cada par (x, y) obtenido de zip(V1, V2), se convierte x e y 
            # a tipo float y se multiplica. Por ejemplo:
            # float(1) * float(4)  # Resultado: 4.0
            #float(2) * float(5)  # Resultado: 10.0
            #float(3) * float(6)  # Resultado: 18.0

            # result = sum(4.0, 10.0, 18.0)  # Resultado: 32.0
            # int(result) convierte el resultado del producto punto a un entero. 
            # int(32.0)  # Resultado: 32

            result = sum(float(x) * float(y) for x, y in zip(V1, V2))
            print(f"Dot product is: {int(result)}")  # Imprime el resultado del producto punto
        except ValueError:
            raise TypeError("All elements must be numeric")  # Manejo de errores si hay elementos no numéricos

    # Decorador para definir un método estático
    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Calcula y muestra la suma de dos vectores.

        Args:
            V1 (list[float]): El primer vector.
            V2 (list[float]): El segundo vector.

        Returns:
            None: Imprime el vector resultante de la suma.

        Raises:
            TypeError: Si las entradas no son listas o contienen valores no numéricos.
            ValueError: Si los vectores tienen diferentes longitudes.
        """
        # Verifica que ambas entradas sean listas
        if not (isinstance(V1, list) and isinstance(V2, list)):
            raise TypeError("Both inputs must be lists")
        
        # Verifica que los vectores tengan la misma longitud
        if len(V1) != len(V2):
            raise ValueError("Vectors must have the same length")
        
        try:
            # Suma los elementos correspondientes de ambos vectores
            # ejmplo si V1 es [1, 2, 3] y V2 es [4, 5, 6], zip(V1, V2) generará el siguiente resultado:
            # [(1, 4), (2, 5), (3, 6)]
            # comprension de la lista 
            # V1 = [1, 2, 3]
            #V2 = [4, 5, 6]
            #result = [float(1) + float(4), float(2) + float(5), float(3) + float(6)]
            # result será: [5.0, 7.0, 9.0]
            #impresion resultado
            # print(f"Add Vector is : {[round(num, 1) for num in [5.0, 7.0, 9.0]]}")
            # Esto imprimirá: "Add Vector is : [5.0, 7.0, 9.0]"
            # [round(num, 1) for num in result] redondea cada número en el resultado a un decimal.
            result = [float(x) + float(y) for x, y in zip(V1, V2)]
            print(f"Add Vector is : {[round(num, 1) for num in result]}")  # Imprime el vector resultante redondeado a 1 decimal
        except ValueError:
            raise TypeError("All elements must be numeric")  # Manejo de errores si hay elementos no numéricos

    # Decorador para definir un método estático
    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Calcula y muestra la resta de dos vectores.

        Args:
            V1 (list[float]): El primer vector.
            V2 (list[float]): El segundo vector.

        Returns:
            None: Imprime el vector resultante de la resta.

        Raises:
            TypeError: Si las entradas no son listas o contienen valores no numéricos.
            ValueError: Si los vectores tienen diferentes longitudes.
        """
        # Verifica que ambas entradas sean listas
        if not (isinstance(V1, list) and isinstance(V2, list)):
            raise TypeError("Both inputs must be lists")
        
        # Verifica que los vectores tengan la misma longitud
        if len(V1) != len(V2):
            raise ValueError("Vectors must have the same length")
        
        try:
            # Resta los elementos correspondientes de ambos vectores
            result = [float(x) - float(y) for x, y in zip(V1, V2)]
            print(f"Sous Vector is: {[round(num, 1) for num in result]}")  # Imprime el vector resultante redondeado a 1 decimal
        except ValueError:
            raise TypeError("All elements must be numeric")  # Manejo de errores si hay elementos no numéricos

# Este bloque se ejecutará si se ejecuta este archivo directamente
if __name__ == "__main__":
    pass  

"""
**kwargs es una convención que se utiliza para pasar un número variable de
 argumentos con nombre (también conocidos como argumentos clave) a una función.
  La sintaxis ** permite que se pasen argumentos como un diccionario, donde 
  cada clave corresponde al nombre del argumento y el valor corresponde al 
  valor que se pasa.
  ejemplo:

def imprimir_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

imprimir_info(nombre="Juan", edad=30, ciudad="Madrid")
 salida:

 nombre: Juan
edad: 30
ciudad: Madrid

ejemplo 2:Combinación con otros parámetro

def funcion_combinada(arg1, arg2, *args, **kwargs):
    print(f"arg1: {arg1}, arg2: {arg2}")
    print("args:", args)
    print("kwargs:", kwargs)

funcion_combinada(1, 2, 3, 4, nombre="Ana", edad=25)

salida
arg1: 1, arg2: 2
args: (3, 4)
kwargs: {'nombre': 'Ana', 'edad': 25}
"""