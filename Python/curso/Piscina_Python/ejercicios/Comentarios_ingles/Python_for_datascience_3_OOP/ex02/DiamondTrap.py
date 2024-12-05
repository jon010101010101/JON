"""
Este módulo define la clase King, que hereda de Baratheon y Lannister.
"""

# Importa las clases Baratheon y Lannister desde el módulo S1E7
from S1E7 import Baratheon, Lannister


# Describe brevemente que este módulo define la clase King, que hereda 
# características de las clases Baratheon y Lannister
class King(Baratheon, Lannister):
    """
    Representa a un personaje Rey, heredando características de Baratheon y
    Lannister.

    Esta clase permite la creación de un Rey con características físicas
    específicas y la capacidad de modificar estas características.
    """

    def __init__(self, first_name: str) -> None:
        """
        Inicializa una instancia de Rey.

        Args:
            first_name (str): El primer nombre del Rey.
        """
        # Llama al constructor de las clases base (Baratheon y Lannister)
        super().__init__(first_name)
        
        # Asigna el nombre de la familia y características físicas específicas
        self.family_name = "Baratheon"  # Nombre de la familia (heredado)
        self.eyes = "brown"              # Color de ojos por defecto
        self.hairs = "dark"              # Color de cabello por defecto

    def set_eyes(self, color: str) -> None:
        """
        Establece el color de ojos del Rey.

        Args:
            color (str): El nuevo color de ojos.
        """
        self.eyes = color  # Asigna el nuevo color a la propiedad eyes

    def set_hairs(self, color: str) -> None:
        """
        Establece el color de cabello del Rey.

        Args:
            color (str): El nuevo color de cabello.
        """
        self.hairs = color  # Asigna el nuevo color a la propiedad hairs

    def get_eyes(self) -> str:
        """
        Obtiene el color actual de los ojos del Rey.

        Returns:
            str: El color actual de los ojos.
        """
        return self.eyes  # Devuelve el valor actual de eyes

    def get_hairs(self) -> str:
        """
        Obtiene el color actual del cabello del Rey.

        Returns:
            str: El color actual del cabello.
        """
        return self.hairs  # Devuelve el valor actual de hairs


def main():
    """
    Función principal para probar la clase King.
    """
    try:
        # Crea una instancia de King con el nombre "Robert"
        robert = King("Robert")

        # Muestra los atributos iniciales del Rey.
        # Modificación de Atributos. Se cambian los colores de ojos y 
        # cabello utilizando los métodos correspondientes.
        print(
            # # define el primer nombre del Rey: Este comentario se refiere
            #  a que robert.first_name accede al atributo first_name del 
            # objeto robert, que contiene el primer nombre del Rey. 
            # En este caso, se espera que sea "Robert"
            f"King: {robert.first_name}, "
            #  define el apellido de la familia: Este comentario puede ser
            # confuso. El apellido no es "King"; en cambio, el atributo
            #  family_name se establece en el constructor de la clase King
            #  como "Baratheon". Esto significa que cuando se imprime 
            # robert.family_name, se mostrará "Baratheon".
            f"Family: {robert.family_name}, "
            f"Eyes: {robert.get_eyes()}, "
            f"Hair: {robert.get_hairs()}"
        )

        # Modifica los atributos del Rey
        robert.set_eyes("green")  # Cambia el color de ojos a verde
        robert.set_hairs("black")  # Cambia el color de cabello a negro

        # Muestra los atributos modificados del Rey
        # Despues de la modificación 
        # El primer nombre seguirá siendo "Robert". 
        # El apellido seguirá siendo "Baratheon". 
        # Los ojos ahora serán "green". 
        # El cabello ahora será "black".
        print(
            f"Modified King: {robert.first_name}, "
            f"Family: {robert.family_name}, "
            f"Eyes: {robert.get_eyes()}, "
            f"Hair: {robert.get_hairs()}"
        )

    except Exception as e:
        print(f"Ocurrió un error: {e}")  # Manejo de errores


if __name__ == "__main__":
    main()  # Ejecuta la función main si el script se ejecuta directamente

