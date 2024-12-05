"""
Este módulo define las clases Baratheon y Lannister,
que heredan de la clase Character.
"""

# Importa la clase Character desde el módulo S1E9
from S1E9 import Character


# define la clase Baratheon, que hereda de la clase base Character. 
# Esto significa que Baratheon tiene acceso a todos los métodos y 
# atributos definidos en Character
class Baratheon(Character):
    """Clase que representa a la familia Baratheon."""

    # Metodo constructor. first_name: El primer nombre del personaje. 
    # is_alive: Un booleano opcional que indica si el personaje está 
    # vivo (por defecto es True)
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Inicializa un personaje de la familia Baratheon.

        Args:
            first_name (str): El primer nombre del personaje.
            is_alive (bool, optional): Indica si el personaje está vivo.
             Por defecto es True.
        """
        # Llama al constructor de la clase base (Character)
        super().__init__(first_name, is_alive)
        
        # Asigna el nombre de la familia y características físicas
        self.family_name = "Baratheon"
        self.eyes = "brown"  # Color de ojos
        self.hairs = "dark"   # Color de cabello

    # Este método devuelve una representación en forma de cadena del objeto,
    #  lo que permite imprimir información útil sobre el objeto cuando se
    #  utiliza con funciones como print().
    # El método devuelve una cadena formateada con los atributos relevantes del personaje
    def __str__(self) -> str:
        """Devuelve una representación en cadena del personaje Baratheon."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    # Este método también devuelve una representación en forma de cadena del
    #  objeto, similar al método anterior. Se utiliza principalmente para 
    # propósitos de depuración y puede ser llamado por funciones como repr().
    def __repr__(self) -> str:
        """Devuelve una representación en cadena del personaje Baratheon."""
        return self.__str__()

    # Este método marca al personaje como muerto.
    def die(self) -> None:
        """Marca al personaje Baratheon como muerto."""
        self.is_alive = False  # Cambia el estado a muerto


# Aquí se define la clase Lannister, que hereda de la clase base Character.
#  Esto significa que Lannister tiene acceso a todos los métodos y atributos
#  definidos en Character.
class Lannister(Character):
    """Clase que representa a la familia Lannister."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Inicializa un personaje de la familia Lannister.

        Args:
            first_name (str): El primer nombre del personaje.
            is_alive (bool, optional): Indica si el personaje está vivo.
             Por defecto es True.
        """
        # Llama al constructor de la clase base (Character)
        super().__init__(first_name, is_alive)
        
        # Asigna el nombre de la familia y características físicas
        self.family_name = "Lannister"
        self.eyes = "blue"   # Color de ojos
        self.hairs = "light"  # Color de cabello

    def __str__(self) -> str:
        """Devuelve una representación en cadena del personaje Lannister."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """Devuelve una representación en cadena del personaje Lannister."""
        return self.__str__()

    def die(self) -> None:
        """Marca al personaje Lannister como muerto."""
        self.is_alive = False  # Cambia el estado a muerto

    # El decorador @classmethod indica que este método es un método de clase.
    #  Esto significa que el método se puede llamar en la clase misma, en lugar
    #  de en una instancia específica de la clase.
    @classmethod
    def create_lannister(
        cls, # representa la propia clase, similar a self. representa a Lanister
        first_name: str, #recibe un parametro para el primer nombre del personaje
        is_alive: bool = True # indica si el personaje esta vivo
    ) -> 'Lannister':
        """
        Crea y devuelve un nuevo personaje Lannister.

        Args:
            first_name (str): El primer nombre del personaje.
            is_alive (bool, optional): Indica si el personaje está vivo.
             Por defecto es True.

        Returns:
            Lannister: Un nuevo personaje Lannister.
        """
        return cls(first_name, is_alive)  # Retorna una nueva instancia de Lannister


def main(): 
    """
    Función principal para probar las clases Baratheon y Lannister.
    """
    try:
        # Prueba la clase Baratheon
        robert = Baratheon("Robert")  # Crea una instancia de Baratheon
        print(robert)  # Imprime la representación del objeto
        robert.die()  # Marca a Robert como muerto
        print(f"Is Robert alive? {robert.is_alive}")  # Verifica si está vivo

        # Prueba la clase Lannister
        cersei = Lannister.create_lannister("Cersei")  # Crea una instancia de Lannister usando el método de clase
        print(cersei)  # Imprime la representación del objeto
        cersei.die()  # Marca a Cersei como muerta
        print(f"Is Cersei alive? {cersei.is_alive}")  # Verifica si está viva

    except Exception as e:
        print(f"An error occurred: {e}")  # Manejo de errores


if __name__ == "__main__":
    main()  # Ejecuta la función principal si el script se ejecuta directamente

