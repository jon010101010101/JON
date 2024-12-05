from typing import Any, Callable
# Any cualquier tipo, se usa cuando no se quiere restringir a un tipo especifico
# callable. es un tipo que representa objetos que pueden ser llamados (como funciones)
# se usa para definir el tipo de function y el tipo de retorno de outer


def square(x: int | float) -> int | float:
    """
    Devuelve el cuadrado de x.

    Args:
        x (int | float): El número que se va a elevar al cuadrado.

    Returns:
        int | float: El cuadrado del número de entrada.
    """
    return x ** 2 * # exponencial, en este caso al cuadrado


def pow(x: int | float) -> int | float:
    """
    Devuelve x elevado a la potencia de x.

    Args:
        x (int | float): La base y el exponente.

    Returns:
        int | float: El resultado de elevar x a la potencia de x.
    """
    return x ** x # ** exponencial. Eleva x a la pontencia de x


def outer(x: int | float,
          function: Callable[[int | float], Any]) -> Callable[[], float]:
    # primer argumento puede ser un int o float
    # Callable. significa que la funcion debe aceptar un argumento int o float
    #  y puede devolver cualquier tipo (Any)
    # -> Callable[[], float]: devulve otra funcion (callable) y que no toma argumentos
    # (por eso []) y devuleve un float

    # Un callable es un objeto que se puede "llamar" como si fuera una función. Esto
    #  significa que puedes usar paréntesis () después del objeto para
    #  ejecutarlo

    # Esta función outer es un ejemplo de una "fábrica de funciones" o "closure". Crea
    #  y devuelve una nueva función que "recuerda" el valor inicial x y la función
    # function. Cada vez que se llame a la función devuelta, aplicará function al 
    # resultado anterior, comenzando con x
    """
    Crea un callable que aplica una función especificada a un valor inicial
    cada vez que se llama, devolviendo el resultado de esa función.

    Args:
        x (int | float): El valor inicial a procesar.
        function (Callable[[int | float], Any]): Una función que toma un número
                                                  y devuelve un número.

    Returns:
        Callable[[], float]: Un objeto callable que devuelve el resultado de
                             aplicar la función al resultado anterior.
    """

    count = 0  # Contador para llevar el registro de llamadas

    # Inicializa previous_result con el valor inicial de x
    previous_result = x # Almacena el resultado de la última operación, inicialmente
    # es x

    def inner() -> float:
        # define funcion inner dentro de la funcion outer, que devuleve un float
        """Función interna que aplica la función dada al resultado anterior."""
        # Declara que count y previous_result son variables que pertenecen al ámbito de
        # la función externa (outer). Permite modificar estas variables desde dentro de
        # inner
        nonlocal count, previous_result
        count += 1  # Incrementa el contador de llamadas cada vez que se llama a inner

        # Calcula el resultado usando la función proporcionada
        result = function(previous_result)

        previous_result = result  # Actualiza previous_result para la próxima llamada
        return result

    return inner  # Devuelve la función interna

# Esta estructura crea un closure. inner "recuerda" y tiene acceso a las variables
#  count, previous_result, y function de su ámbito externo, incluso después de que
#  outer haya terminado de ejecutarse. Cada vez que se llama a la función devuelta
#  por outer, se ejecuta inner, que mantiene un estado interno entre llamadas.
# Este patrón es útil para crear funciones que mantienen un estado interno sin usar
#  variables globales,

"""
Este código implementa un patrón de diseño interesante que combina el uso de funciones
 de orden superior, closures, y callables. Vamos a resumir sus características
  principales:

    Función outer:
        Es una función de orden superior que toma dos argumentos:
            x: Un valor inicial (int o float)
            function: Una función callable que opera sobre números
        Retorna otra función (inner) que es callable
    Función inner (closure):
        Es definida dentro de outer y tiene acceso a las variables del ámbito
         de outer
        Mantiene un estado interno (previous_result y count)
        Cada vez que se llama, aplica la función pasada a outer al resultado
         anterior
        Actualiza el estado interno para la próxima llamada
    Comportamiento del callable retornado:
        Cuando se llama a outer, devuelve inner como un callable
        Cada llamada subsiguiente a este callable (inner) realiza lo siguiente:
            Incrementa un contador interno
            Aplica la función dada al resultado anterior
            Actualiza el resultado para la próxima llamada
            Devuelve el nuevo resultado
    Manejo de errores:
        Verifica que los resultados sean numéricos en cada paso
        Imprime mensajes de error si los resultados no son numéricos

En resumen, este código crea una especie de "generador de secuencia" personalizado.
 Cada vez que se llama al callable retornado, genera el siguiente número en una 
 secuencia definida por la función inicial y el valor inicial. Por ejemplo:

    Con square, genera una secuencia donde cada número es el cuadrado del anterior.
    Con pow, genera una secuencia donde cada número es elevado a sí mismo.

Este patrón es útil para crear secuencias personalizadas, implementar cálculos 
iterativos, o crear funciones que mantienen un estado interno entre llamadas, 
todo ello de una manera flexible y reutilizable.

el concepto de callables es fundamental para el funcionamiento de este patrón. La 
función outer toma un callable como argumento y devuelve otro callable, creando 
así una cadena de funciones que pueden ser llamadas sucesivamente.
"""