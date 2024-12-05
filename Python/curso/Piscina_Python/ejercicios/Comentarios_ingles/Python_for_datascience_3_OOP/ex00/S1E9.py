class Character:
    """Clase que representa un personaje en el universo de Game of Thrones."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Inicializa un personaje.

        Args:
            first_name (str): El primer nombre del personaje.
            is_alive (bool, optional): Indica si el personaje está vivo.
                Por defecto es True.

        Raises:
            ValueError: Si first_name está vacío o no es una cadena.
            TypeError: Si is_alive no es un booleano.
        """
        # Verifica que first_name sea una cadena no vacía
        if not isinstance(first_name, str) or not first_name:
            raise ValueError("El nombre debe ser una cadena no vacía.")
        
        # Verifica que is_alive sea un booleano
        if not isinstance(is_alive, bool):
            raise TypeError("is_alive debe ser un booleano.")
        
        # Asigna los atributos del personaje
        # Al usar self, estamos indicando que queremos asignar valores
        #  a los atributos que pertenecen a la instancia específica del
        #  objeto que estamos creando
        self.first_name = first_name
        self.is_alive = is_alive

    # instancia" se refiere a un objeto creado a partir de una clase

    #dentro de una clase se definen metodos. Self se refiere a la 
    # instancia actual, y none es que no retornan nada
    def die(self) -> None:
        """Marca al personaje como muerto."""
        self.is_alive = False #false indica que ha muerto


# class Stark(Character) define la clase Stark, que hereda de la clase 
# Character. Esto significa que Stark es una subclase de Character y, 
# por lo tanto, hereda todos los atributos y métodos de Character.
# La herencia permite que Stark utilice las funcionalidades definidas 
# en Character, como el atributo is_alive y el método die.
class Stark(Character):
    """Clase que representa un personaje de la familia Stark."""

    def die(self) -> None:
        """Marca al personaje Stark como muerto."""
        super().die()  # Llama al método de la clase base


def main():
    """
    Función principal para demostrar el uso de las clases Character y Stark.
    """
    try:
        # Crea y prueba una instancia de Character
        ned = Character("Ned")
        print(f"Personaje: {ned.first_name}, Vivo: {ned.is_alive}")
        
        # Llama al metodo die para marca al personaje como muerto
        ned.die()
        # Imprime nuevamente el estado del personaje después de llamar a die().
        print(f"Después de morir: {ned.first_name}, Vivo: {ned.is_alive}")

        # Crea y prueba una instancia de Stark
        arya = Stark("Arya")
        print(f"Stark: {arya.first_name}, Vivo: {arya.is_alive}")
        
        # Marca al personaje Stark como muerto
        arya.die()
        print(f"Después de morir: {arya.first_name}, Vivo: {arya.is_alive}")

        # Prueba el manejo de errores
        try:
            # intenta crear un personaje con un nombre vacío, lo que debería 
            # lanzar un ValueError.
            Character("")
        except ValueError as e:
            print(f"Error esperado capturado: {e}")

        try:
            #  intenta crear una instancia de Stark con un valor no booleano
            #  para el parámetro is_alive, lo que debería lanzar un TypeError
            Stark("Inválido", is_alive="No es un booleano")
        except TypeError as e:
            print(f"Error esperado capturado: {e}")
    # captura cualquier otra excepción no manejada que pueda ocurrir durante
    # la ejecución del código dentro del bloque try. Esto asegura que si hay
    # errores inesperados,se informen adecuadamente sin interrumpir 
    # abruptamente el programa.
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


# verifica si este archivo se está ejecutando directamente. Si es así, 
# llama a la función main(), iniciando así la ejecución del programa.
if __name__ == "__main__":
    main()
