"""
from S1E9 import Character, Stark

    Importa las clases Character y Stark del módulo S1E9.

Ned = Stark("Ned")

    Crea una instancia de la clase Stark llamada Ned.

print(Ned.__dict__)

    Imprime el diccionario de atributos de Ned.
    Resultado esperado: {'first_name': 'Ned', 'is_alive': True}
    Esto muestra que Ned tiene un nombre "Ned" y está vivo por defecto.

print(Ned.is_alive)

    Imprime el estado de vida de Ned.
    Resultado esperado: True
    Confirma que Ned está vivo inicialmente.

Ned.die()

    Llama al método die() en Ned, cambiando su estado a muerto.

print(Ned.is_alive)

    Imprime el estado de vida actualizado de Ned.
    Resultado esperado: False
    Muestra que Ned ahora está muerto después de llamar a die().

print(Ned.__doc__)

    Imprime el docstring de la clase Stark.
    Resultado: El docstring definido para la clase Stark.

print(Ned.__init__.__doc__)

    Imprime el docstring del método constructor de Stark.
    Resultado: El docstring definido para el método init de Stark.

print(Ned.die.__doc__)

    Imprime el docstring del método die de Stark.
    Resultado: El docstring definido para el método die de Stark.

print("---")

    Imprime una línea de separación.

Lyanna = Stark("Lyanna", False)

    Crea una instancia de Stark llamada Lyanna, inicializada como muerta (False).

print(Lyanna.__dict__)

    Imprime el diccionario de atributos de Lyanna.
    Resultado esperado: {'first_name': 'Lyanna', 'is_alive': False}
    Muestra que Lyanna tiene el nombre "Lyanna" y está inicializada como muerta.


"""
