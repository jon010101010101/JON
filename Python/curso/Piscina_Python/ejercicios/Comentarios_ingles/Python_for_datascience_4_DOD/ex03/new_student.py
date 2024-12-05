import random
import string
from dataclasses import dataclass, field


def generate_random_id() -> str:
    """
    Genera un ID de estudiante aleatorio de 15 caracteres que consiste en
    letras minúsculas y dígitos.

    Returns:
        str: Un ID de estudiante generado aleatoriamente.
    """
    return ''.join(
        random.choices(string.ascii_lowercase + string.digits, k=15)
    )


@dataclass
class Student:
    """Representa a un estudiante."""

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)  # Campo que se inicializa después
    # ID generado automáticamente
    id: str = field(init=False, default_factory=generate_random_id)

    def __post_init__(self):
        """
        Inicializa el atributo login basado en el nombre y apellido
         del estudiante.
        """
        self.login = f"{self.name[0].upper()}{self.surname.lower()}"


def main():
    """
    Función principal para ejecutar pruebas y manejar errores.
    """
    # Caso 1: Crear un estudiante válido
    student1 = Student(name="Edward", surname="agle")
    print(student1)  # Esto mostrará todos los atributos del estudiante

    # Caso 2: Intentar crear un estudiante con un argumento no válido
    try:
        # Esto causará un error, por tener id
        student2 = Student(name="Alice", surname="Smith")  # No se pasa 'id'
        print(student2)  # Esto debería ejecutarse correctamente
    except TypeError as e:
        # Captura y muestra el mensaje de error específico
        print(f"Error: {e}")


if __name__ == "__main__":
    main()


"""
Para que la clase Student detecte si se pasa un argumento no válido
como id al momento de crear una instancia, y para que se maneje este
caso de manera que se imprima un mensaje de error específico sin mostrar
el traceback completo, puedes implementar la lógica de manejo de
excepciones en el método __post_init__. Sin embargo, dado que el
decorador @dataclass genera automáticamente el método __init__, no
puedes modificarlo directamente.
"""
