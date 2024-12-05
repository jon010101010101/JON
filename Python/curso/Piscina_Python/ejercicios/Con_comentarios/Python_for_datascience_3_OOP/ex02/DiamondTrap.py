"""
Este módulo define la clase Rey, que hereda de Baratheon y Lannister.
"""

from S1E7 import Baratheon, Lannister


# Herencia Múltiple: La clase Rey hereda de dos clases: Baratheon y Lannister.
#  Esto significa que un objeto de la clase Rey tendrá acceso a los atributos y
#  métodos definidos en ambas clases
class Rey(Baratheon, Lannister):
    """
    Representa un personaje Rey, heredando rasgos de Baratheon y Lannister.

    Esta clase permite la creación de un Rey con rasgos físicos específicos
    y la capacidad de modificar estos rasgos.
    """

    def __init__(self, nombre: str) -> None:
        """
        Inicializa una instancia de Rey.

        Args:
            nombre (str): El nombre del Rey.
        """
        # super().__init__(first_name) intenta llamar al constructor de la clase 
        # base. Sin embargo, hay un error aquí porque first_name no está definido
        #  en este contexto; debería ser nombre
        super().__init__(first_name)
        #self.family_name = "Baratheon" # Establece el apellido del rey como "Baratheon".
        #self.eyes = "brown" # Establece el color de ojos como marrón.
        #self.hairs = "dark" # Establece el color de cabello como oscuro.
        #estass no hace falta ponerlas por que ya las hereda
   
        # Supongamos que tenemos una clase Rey definida previamente.
        #rey = Rey("Robert")  # Crear una instancia de Rey llamada Robert.

        # Establecer el color de ojos usando set_eyes.
        #rey.set_eyes("green")  # Cambia el color de ojos a "green".

        # Obtener el nuevo color de ojos usando get_eyes.
        #color_actual = rey.get_eyes()  # Llama a get_eyes para obtener el color
        #  actual.

        # Imprimir el nuevo color de ojos.
        #print(f"El color de ojos actual del Rey es: {color_actual}")  

        # Imprime: "El color de ojos actual del Rey es: green"

    def set_eyes(self, color: str) -> None:
        """
        Set the eye color of the King.

        Args:
            color (str): The new eye color.
        """
        self.eyes = color

    def set_hairs(self, color: str) -> None:
        """
        Set the hair color of the King.

        Args:
            color (str): The new hair color.
        """
        self.hairs = color

    def get_eyes(self) -> str:
        """
        Get the current eye color of the King.

        Returns:
            str: The current eye color.
        """
        return self.eyes

    def get_hairs(self) -> str:
        """
        Get the current hair color of the King.

        Returns:
            str: The current hair color.
        """
        return self.hairs


def main():
    """
    Función principal para probar la clase Rey.
    """
    try:
        # Crear una instancia de Rey
        robert = King("Robert")

        # Mostrar atributos iniciales
        print(
            f"King: {robert.first_name}, " # Robert
            f"Family: {robert.family_name}, " # baratheon, establecido por el constructor
            f"Eyes: {robert.get_eyes()}, " # marron, establecido por el constructor
            f"Hair: {robert.get_hairs()}" #oscuro, establecido por el constructor
        )

        # Modificar atributos
        robert.set_eyes("green")
        robert.set_hairs("black")

        # Mostrar atributos modificados
        print(
            f"Modified King: {robert.first_name}, " # Robert
            f"Family: {robert.family_name}, " # baratheon
            f"Eyes: {robert.get_eyes()}, " # verdes
            f"Hair: {robert.get_hairs()}" # negro
        )

    except Exception as e:
        print(f"Ocurrió un error: {e}")


if __name__ == "__main__":
    main()

