from typing import Any, Callable, TypeVar, cast
# Callable se utiliza para tipar funciones y decoradores.

# TypeVar. se usa para crear variables de tipo (tipos genéricos o polimórficos)
# Es útil para crear decoradores o funciones que preservan el tipo de sus argumentos.
# Ejemplo: T = TypeVar('T') # def identity(x: T) -> T:

# cast es una función que se usa para indicar al verificador de tipos que una expresión
#  debe ser tratada como si tuviera un tipo específico.
# No realiza ninguna conversión en tiempo de ejecución, solo es una indicación para
#  herramientas de análisis estático.
# Ejemplo: x = cast(int, some_function())

F = TypeVar('F', bound=Callable[..., Any])
# TypeVar es una función del módulo typing que se utiliza para crear variables de
#  tipo genérico. Permite definir un tipo que puede ser utilizado en diferentes contextos,
#  facilitando la creación de funciones y clases que pueden operar con diferentes
#  tipos de datos.

# F variable que estamos definiendo

# bound=Callable[..., Any] significa que F debe ser un tipo que sea callable (es 
# decir, una función) que puede aceptar cualquier número y tipo de argumentos (...)
#  y devolver cualquier tipo (Any).

# Es una herramienta poderosa en Python para trabajar con funciones genéricas. Permite
#  definir tipos que son más específicos y útiles en contextos donde se manipulan
# funciones como objetos, garantizando al mismo tiempo la flexibilidad y la seguridad
#  tipográfica.


def callLimit(limit: int) -> Callable[[F], F]:
    """
    Decorador que limita el número de veces que se puede llamar a una función.

    Args:
        limit (int): El número máximo de veces que se puede llamar a la función.

    Returns:
        Callable[[F], F]: Una función decoradora que envuelve la función original.
    """
    def callLimiter(function: F) -> F:
        """
        Función envoltura que implementa el límite de llamadas.

        Args:
            function (F): La función que se va a envolver.

        Returns:
            F: La función envuelta con la funcionalidad de límite de llamadas.
        """
        count = 0 # Inicializa un contador para llevar el registro de cuántas veces se 
                  # ha llamado a la función

        def limit_function(*args: Any, **kwds: Any) -> Any:
            """
            Función interna que verifica el conteo de llamadas y ejecuta la función original.

            Args:
                *args: Lista de argumentos de longitud variable.
                **kwds: Argumentos clave arbitrarios.

            Returns:
                Any: El resultado de la función original, si se llama dentro del límite.
            """
            nonlocal count # Permite modificar la variable count de la función envoltura
            if count < limit:  # Verifica si el contador es menor que el límite permitido
                count += 1 # Incrementa el contador en 1
                return function(*args, **kwds)  # Llama a la función original con los 
                                                # argumentos proporcionados
            else: # Si se ha alcanzado el límite, imprime un mensaje de error
                print(f"Error: <function {function.__name__} at "
                      f"{hex(id(function))}> se ha llamado demasiadas veces")

        # Preservar los metadatos de la función original
        # Copia el nombre de la función original
        limit_function.__name__ = function.__name__
        # Copia la documentación de la función original
        limit_function.__doc__ = function.__doc__

        return cast(F, limit_function) # # Devuelve la función envoltura como tipo F

    return callLimiter # # Devuelve el decorador callLimiter
    # decorador es una función que toma otra función como argumento y devuelve una
    #  nueva función que generalmente agrega alguna funcionalidad al comportamiento
    #  original. Esto permite "decorar" la función original con nuevas capacidades.
"""
Uso de Wrappers (envoltura):

    La función limit_function actúa como un wrapper (envoltura) alrededor
    de la función original. Verifica el conteo de llamadas y, si no se ha
    alcanzado el límite, ejecuta la función original; de lo contrario,
    imprime un mensaje de error.
    
    Los wrappers son útiles para agregar funcionalidad (como contar
    llamadas) mientras se preserva el comportamiento original de la función.
"""
Para asegurarse de que la clase Student detecte si se pasa un argumento
inválido como 'id' al crear una instancia, y para manejar este caso de
manera que se imprima un mensaje de error específico sin mostrar el
traceback completo, puedes implementar una lógica de manejo de excepciones
en el método post_init. Sin embargo, dado que el decorador @dataclass
 genera automáticamente el método init, no puedes modificarlo directamente.

 """
 Esta función implementa un decorador llamado callLimit que limita el número de veces
  que una función puede ser llamada. Aquí está un resumen de lo que hace:

    Definición del decorador:
        callLimit(limit) es un decorador que toma un argumento limit, que es el número
         máximo de veces que se permite llamar a la función decorada.
    Contador de llamadas:
        Utiliza una variable count para llevar un registro del número de veces que se
         ha llamado la función.
    Función interna callLimiter:
        Esta es la función que realmente decora la función original.
        Crea una nueva función limit_function que envuelve la función original.
    Función limit_function:
        Verifica si se ha alcanzado el límite de llamadas.
        Si no se ha alcanzado el límite, incrementa el contador y llama a la función
         original.
        Si se ha alcanzado el límite, imprime un mensaje de error y no llama a la 
        función original.
    Uso del decorador:
        Se puede aplicar a cualquier función usando la sintaxis @callLimit(n), donde 
        n es el número máximo de llamadas permitidas.
    Función main:
        Demuestra el uso del decorador con dos funciones de ejemplo, f() y g().
        f() está limitada a 3 llamadas, mientras que g() está limitada a 1 llamada.
    Manejo de errores:
        Utiliza un bloque try-except para capturar cualquier error inesperado durante
         la ejecución.

En resumen, este código implementa un mecanismo para limitar el número de veces que
 se puede llamar a una función, lo cual puede ser útil para controlar el uso de 
 recursos, implementar lógica de negocio específica, o para propósitos de depuración
  y pruebas. El uso de decoradores permite aplicar esta funcionalidad de manera limpia
   y reutilizable a diferentes funciones.
 
 """