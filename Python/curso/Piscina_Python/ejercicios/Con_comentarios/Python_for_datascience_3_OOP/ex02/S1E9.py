# from abc import: Esta parte indica que estamos importando algo del módulo abc.
#  El módulo abc es parte de la biblioteca estándar de Python y proporciona
#  infraestructura para definir clases base abstractas.

# ABC: Es una clase que se importa del módulo abc. ABC significa "Abstract Base
#  Class" (Clase Base Abstracta). Es una clase auxiliar que se utiliza como base
#  para crear clases abstractas en Python.

# abstractmethod: Es un decorador que también se importa del módulo abc.
# Se utiliza para declarar métodos abstractos dentro de una clase abstracta.

# El uso de clases abstractas y métodos abstractos en Python permite:

    # Definir una interfaz común para un grupo de subclases.
    # Forzar a las subclases a implementar ciertos métodos.
    # Prevenir la instanciación directa de la clase base abstracta.

#Esta funcionalidad es útil para diseñar jerarquías de clases bien estructuradas
# y para asegurar que las subclases cumplan con un contrato específico definido
# en la clase base abstracta.

from abc import ABC, abstractmethod

# Paso 1: Definir la clase base abstracta Character
class Character(ABC):
    """Clase base abstracta que representa un personaje en el universo de 
    Juego de Tronos."""

    # self es el primer parámetro de cualquier método de instancia en Python. 
    # Representa la instancia que se esta creando y Python lo hace automaticamente.
    # Toma dos parámetros: first_name (obligatorio) e is_alive (opcional con valor
    #  predeterminado True).
    # Utiliza anotaciones de tipo para indicar que first_name debe ser una cadena
    #  y is_alive un booleano.
    # No devuelve ningún valor (lo cual es estándar para los constructores en 
    # Python).
    
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Tu docstring para el Constructor"""
        """
        Inicializa un personaje.

        Args:
            first_name (str): El primer nombre del personaje.
            is_alive (bool, opcional): Indica si el personaje está vivo.
                Por defecto es True.

        Raises:
            ValueError: Si first_name está vacío o no es una cadena.
            TypeError: Si is_alive no es un booleano.
        """
        # Paso 2: Validar los argumentos de entrada
        if not isinstance(first_name, str) or not first_name:
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(is_alive, bool):
            raise TypeError("is_alive debe ser un booleano.")

        # Paso 3: Asignar los atributos
        # # esta línea está guardando el nombre proporcionado al crear
        # el objeto como un atributo de la instancia.
        self.first_name = first_name
        self.is_alive = is_alive

    # Crea un metodo abstracto (una funcion dentro de una clase), que crea 
    # un esqueleto para futura implementacion. El @abstractmethod indica que 
    # cualquier clase que herede de Character debe proporcionar su propia 
    # implementación de este método. Pass que no se implementta aqui.
    @abstractmethod
    def die(self) -> None:
        """
        Método abstracto para marcar al personaje como muerto.
        Este método debe ser implementado por todas las subclases.
        """
        pass 
    # El pass aquí significa que no hay implementación en la clase base abstracta.


# Paso 4: Definir la clase Stark que hereda de Character sus atributos y metodos
# Stark que hereda de la clase abstracta Character. Implementa el método abstracto
#  die, proporcionando una funcionalidad específica para los personajes Stark. 
# Esta implementación permite que los objetos de la clase Stark puedan "morir", 
# cambiando su estado de vida a falso.
class Stark(Character):
    """Tu docstring para la Clase"""
    """Clase que representa un personaje de la familia Stark."""

    def die(self) -> None:
        """Tu docstring para el Método"""
        """Marca al personaje Stark como muerto."""
        # Paso 5: Implementar el método die para los personajes Stark
        self.is_alive = False

# Paso 6: Definir la función principal
def main():
    """
    Función principal para demostrar el uso de las clases Character y Stark.
    """
    try:
        # Paso 7: No podemos crear una instancia de Character ya que es abstracta
        # ned = Character("Ned")  # Esto generaría un error

        # Paso 8: Crear y probar una instancia de Stark
        # Crea una instancia de Stark llamada arya.
        # Imprime el estado inicial de arya que ha heredado por su clase
        # Llama al método die() en arya. Con lo que cambia atributo de viva a muerta
        # Imprime el estado de arya después de llamar a die(). Muerta
        arya = Stark("Arya")
        print(f"Stark: {arya.first_name}, Alive: {arya.is_alive}")
        arya.die()
        print(f"Después de morir(): {arya.first_name}, Alive: {arya.is_alive}")

        # Paso 9: Probar el manejo de errores
        try:
            # intenta crear un Stark con un nombre vacío, lo que debería lanzar 
            # un ValueError
            Stark("")
        except ValueError as e:
            print(f"Error esperado capturado: {e}")

        try:
            # intenta crear un Stark con un valor no booleano para is_alive, 
            # lo que debería lanzar un TypeError.
            Stark("Inválido", is_alive="No es un booleano")
        except TypeError as e:
            print(f"Error esperado capturado: {e}")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Paso 10: Ejecutar la función principal si este script es el programa principal
if __name__ == "__main__":
    main()
