from typing import Any, Callable

"""
Uso de Wrappers (envoltura):

    La función limit_function actúa como un wrapper (envoltura) alrededor
    de la función original. Verifica el conteo de llamadas y, si no se ha
    alcanzado el límite, ejecuta la función original; de lo contrario,
    imprime un mensaje de error.
    Los wrappers son útiles para agregar funcionalidad (como contar
    llamadas) mientras se preserva el comportamiento original de la función.
"""


def callLimit(limit: int):
    """
    Decorador que limita el número de veces que se puede llamar a una función.

    Args:
        limit (int): El número máximo de veces que se permite llamar a
        la función decorada.

    Returns:
        Callable: Un decorador que aplica la limitación a la función.
    """

    count = 0  # Contador para llevar el control de las llamadas

    def callLimiter(function: Callable) -> Callable:
        """
        Función decoradora que limita las llamadas a la función original.

        Args:
            function (Callable): La función a la que se aplicará el límite.

        Returns:
            Callable: La función limitada.
        """

        def limit_function(*args: Any, **kwds: Any) -> None:
            """Función interna que controla el número de llamadas."""
            # Permite modificar el contador en el ámbito externo
            nonlocal count

            # Manejo de errores para asegurar que no se exceda el límite
            if count >= limit:
                print(f"Error: {repr(function)} call too many times.")
                return  # Si se alcanza el límite, no se llama a la función

            count += 1  # Incrementa el contador
            return function(*args, **kwds)  # Llama a la función original

        return limit_function  # Retorna la función limitada

    return callLimiter  # Retorna el decorador


def main():
    """
    Función principal para probar el decorador callLimit con varias funciones.
    """
    try:
        @callLimit(3)
        def f():
            """Imprime un mensaje al ser llamada."""
            print("f()")

        @callLimit(1)
        def g():
            """Imprime un mensaje al ser llamada."""
            print("g()")

        # Prueba de las funciones decoradas
        for i in range(3):
            f()  # Debería imprimir "f()" hasta 3 veces
            g()  # Debería imprimir "g()" solo una vez

    except Exception as e:
        # Manejo de errores inesperados
        print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    main()
