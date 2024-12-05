from typing import Any, Callable


def square(x: int | float) -> int | float:
    """
    Retorna el cuadrado de x. 

    Args:
        x (int | float): El número a ser elevado al cuadrado.

    Returns:
        int | float: El cuadrado del número de entrada.
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """
    Retorna x elevado a la potencia de x.

    Args:
        x (int | float): La base y el exponente.

    Returns:
        int | float: El resultado de elevar x a la potencia de x.
    """
    return x ** x


def outer(
    x: int | float,
    function: Callable[[int | float], Any]
) -> Callable[[], float]:
# x es un int o foat
# funtion es un parametro que espera una funcion callable
# Callable[[int | float], Any]. la funcion debe aceptar un int o float y puede 
# devolver cualquier Any
# la funcion outer devuelve otra función (un callable).
# Esta función devuelta no toma argumentos ([]) y devuelve un float.

    """
    Crea un callable que aplica una función especificada a un valor inicial
    cada vez que se llama, devolviendo el resultado de esa función.

    Args:
        x (int | float): El valor inicial a ser procesado.
        function (Callable[[int | float], Any]): Una función que toma un número
                                                  y devuelve un número.

    Returns:
        Callable[[], float]: Un objeto callable que devuelve el resultado de
                             aplicar la función al resultado anterior.
    """

    # Inicializa el contador y el resultado previo
    count = 0
    previous_result = x

    def inner() -> float: #inner es una funcion anidada dentro de outer
        """Función interna que aplica la función dada al resultado previo."""
        nonlocal count, previous_result # son variable definidas en el exterior
        # en outer, pero no global, permite a inner modificar estas variables
        # en el ambito de la fnción que la contiene
        count += 1  # Incrementa el contador cada vez que se llama inner

        # Manejo de errores para asegurar que previous_result sea numérico
        if not isinstance(previous_result, (int, float)):
            print("ERROR: El resultado previo no es numérico.")
            return None

        # Calcula el resultado usando la función proporcionada
        result = function(previous_result)

        # Manejo de errores para asegurar que el resultado sea numérico
        if not isinstance(result, (int, float)):
            print("ERROR: El resultado de la función no es numérico.")
            return None

        # Actualiza previous_result para la siguiente llamada
        previous_result = result
        return result

    return inner


def main():
    """
    Función principal para probar las funciones square, pow y outer
    con varios inputs y manejo de errores.
    """
    try:
        my_counter = outer(3, square)
        print(my_counter())  # Debería imprimir 9 (3^2)
        print(my_counter())  # Debería imprimir 81 (9^2)
        print(my_counter())  # Debería imprimir 6561 (81^2)
        print("---")

        another_counter = outer(1.5, pow)
        # Debería imprimir aproximadamente 1.837
        print(another_counter())  # (1.5^1.5)
        # Debería imprimir aproximadamente 2.755
        print(another_counter())  # (1.837^1.837)

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    main()

"""
término callable se refiere a cualquier objeto que puede ser llamado como
 si fuera una función. Esto incluye funciones, métodos y objetos de clases
  que implementan el método especial __call__().

 Qué es un Callable?

    Definición:
        Un objeto es considerado callable si se puede invocar utilizando paréntesis, como en objeto().
        Los ejemplos más comunes de objetos callables son las funciones y los métodos.
    Ejemplos de Callables:
        Funciones:

        python
        def suma(a, b):
            return a + b

        resultado = suma(2, 3)  # suma es callable

Métodos de Clase:

python
class Calculadora:
    def multiplicar(self, a, b):
        return a * b

calc = Calculadora()
resultado = calc.multiplicar(2, 3)  # multiplicar es callable

Objetos con __call__:
Puedes definir una clase que implemente el método __call__, lo que permite que sus instancias sean llamadas como funciones.

python
class FuncionCuadrado:
    def __call__(self, x):
        return x ** 2

cuadrado = FuncionCuadrado()
resultado = cuadrado(4)  # cuadrado es callable

Verificación de Callables:

    Puedes verificar si un objeto es callable utilizando la función callable():

    python
    print(callable(suma))  # True
    print(callable(calc.multiplicar))  # True
    print(callable(cuadrado))  # True

"""