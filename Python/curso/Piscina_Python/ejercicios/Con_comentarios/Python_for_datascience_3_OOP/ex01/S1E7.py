"""
Este módulo define las clases Baratheon y Lannister,
que heredan de la clase Character.
"""

from S1E9 import Character


class Baratheon(Character):
    """Representa a la familia Baratheon."""

    def __init__(self, nombre: str, esta_vivo: bool = True) -> None:
        """
        Inicializa un personaje Baratheon.

        Args:
            nombre (str): El nombre del Character.
            esta_vivo (bool, opcional): Si el personaje está vivo.
             Por defecto es True.
        """
        # super() es una función especial en Python que se refiere a la clase 
        # padre (en este caso, Character).
        # .init__(nombre, esta_vivo) llama al método constructor (__init__) de 
        # la clase padre
        super().__init__(first_name, is_alive)
        # Una vez se inician los atributos del padre clase Character, se le añaden 
        # atributos especificos nombre familia Baratheon que tendrán ojos marrones
        #  y pelo negro
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    # Crea un vector con los atributos nuevos creados formateada f-string
    # Vector: ('Baratheon', 'marrones', 'oscuro')
    def __str__(self) -> str:
        """Devuelve una representación en cadena del Character Baratheon."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    # este método __repr__ está configurado para proporcionar la misma representación
    # en cadena que __str__, asegurando una consistencia en la forma en que el objeto
    # Baratheon se representa como string en diferentes contextos de Python.
    def __repr__(self) -> str:
        """Devuelve una representación en cadena del Character Baratheon."""
        return self.__str__()

    # Cambia el atributo de la clase Baratheon para ponerlos como muertos
    def die(self) -> None:
        """Marca al Character Baratheon como muerto."""
        self.is_alive = False


class Lannister(Character):
    """Representa a la familia Lannister."""

    def __init__(self, nombre: str, esta_vivo: bool = True) -> None:
        """
        Inicializa un (personaje) Character Lannister.

        Args:
            nombre (str): El nombre del personaje.
            esta_vivo (bool, opcional): Si el personaje está vivo.
             Por defecto es True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self) -> str:
        """Devuelve una representación en cadena del personaje Lannister."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')

    def __repr__(self) -> str:
        """Devuelve una representación en cadena del personaje Lannister."""
        return self.__str__()

    def die(self) -> None:
        """Marca al personaje Lannister como muerto."""
        self.is_alive = False

    # este método es una forma alternativa de crear instancias de Lannister,
    # proporcionando una interfaz de fábrica para la creación de personajes
    #  Lannister. No modifica el atributo die ni cambia el estado de vida de
    #  un personaje existente, sino que crea un nuevo personaje con los atributos
    #  especificados.
    # @classmethod Este decorador indica que el método siguiente es un método 
    # de clase.
    # cls: Representa la clase en la que se define el método.
    @classmethod
    def crear_lannister(
        cls,
        nombre: str,
        esta_vivo: bool = True
    ) -> 'Lannister':
        """
        Crea y devuelve un nuevo personaje Lannister.

        Args:
            nombre (str): El nombre del personaje.
            esta_vivo (bool, opcional): Si el personaje está
             vivo. Por defecto es True.

        Returns:
            Lannister: Un nuevo personaje Lannister.
        """
        # crea y devuelve una nueva instancia de la clase Lannister.
        return cls(first_name, is_alive)


def main():
    """
    Función principal para probar las clases Baratheon y Lannister.
    """
    try:
        # Test Baratheon
        # Crea un personaje Baratheon llamado Robert.
        # Por defecto, estará vivo (is_alive = True).
        # Heredará los atributos de los Baratheon: ojos marrones y cabello oscuro.

        robert = Baratheon("Robert")
        print(robert) # imprime la representacion de Robert
        robert.die() # Ahora sera muerto
        print(f"Is Robert alive? {robert.is_alive}")

        # Test Lannister
        # Crea un personaje Lannister llamado Cersei usando el método de clase 
        # create_lannister.
        # Por defecto, Cersei estará viva (is_alive = True).
        # Heredará los atributos de los Lannister: ojos azules y cabello claro.

        cersei = Lannister.create_lannister("Cersei")
        print(cersei) # imprime la representacion de cersei
        cersei.die() # Ahora será muerto
        print(f"Is Cersei alive? {cersei.is_alive}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
