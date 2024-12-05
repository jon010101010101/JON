import random # Importa el módulo random para generar valores aleatorio
import string # Importa el módulo string para acceder a constantes de cadenas
from dataclasses import dataclass, field  # Importa decoradores y funciones 
                                        # para crear clases de dato


def generate_random_id() -> str:
    # define una funcion que no toma ningun argumenteo que devuleve un valor tipo str
    """
    Genera un ID de estudiante aleatorio de 15 caracteres que consiste en
    letras minúsculas y dígitos.

    Returns:
        str: Un ID de estudiante generado aleatoriamente.
    """
    return ''.join(
        random.choices(string.ascii_lowercase + string.digits, k=15)
    )
    # random.choices() es una función del módulo random que permite seleccionar
    # elementos al azar de una secuencia (como una lista o una cadena). Esta 
    # función puede seleccionar múltiples elementos, y permite que los mismos 
    # elementos sean seleccionados más de una vez.

    # string.ascii_lowercase: Esta constante contiene todas las letras minúsculas
    #  del alfabeto inglés, es decir, 'abcdefghijklmnopqrstuvwxyz'.

    # string.digits: Esta constante contiene todos los dígitos decimales, es 
    # decir, '0123456789'

    # con el join concatenamos estas dos cadenas, obtenemos un conjunto de 
    # caracteres que incluye tanto letras minúsculas como dígitos: 
    # 'abcdefghijklmnopqrstuvwxyz0123456789'

    # k=15 Este argumento especifica cuántos elementos se deben seleccionar 
    # al azar de la secuencia proporcionada.


@dataclass
# @dataclass: Este decorador se utiliza para convertir la clase Student en una
#  clase de datos. Esto significa que Python generará automáticamente métodos 
# especiales como __init__, __repr__, __eq__, entre otros, basándose en los 
# atributos definidos en la clase
class Student:
    """
    Representa a un estudiante con su nombre, apellido, estado activo,
    login y un ID único.

    Attributes:
        name (str): El primer nombre del estudiante.
        surname (str): El apellido del estudiante.
        active (bool): Indica si el estudiante está activo (por defecto 
        es True).
        login (str): El login del estudiante, generado a partir del nombre 
        y apellido.
        id (str): Un identificador único para el estudiante, generado 
        automáticamente.
    """

    name: str # atributo donde se almacenara el nombre
    surname: str # atributo donde se almacenara el apellido
    active: bool = True  # Estado activo del estudiante
    login: str = field(init=False)  # Login generado automáticamente,
                                    # no se inicializa en el constructor
    id: str = field(init=False, default_factory=generate_random_id)  
    # ID generado automáticamente utilizando la función generate_random_id

    def __post_init__(self):
        # Este método se llama automáticamente después de que se han inicializado
        #  los atributos de la clase. Es útil para realizar operaciones adicionales
        #  o cálculos basados en los valores iniciales proporcionados.
        """
        Genera automáticamente el login del estudiante basado en su nombre
        y apellido. El formato del login es la primera letra del nombre
        seguida del apellido en minúsculas.
        """
        self.login = f"{self.name[0].upper()}{self.surname.lower()}" 
         # Asigna el login
         # Asigna el login utilizando la primera letra del nombre (en mayúscula)
         # seguida del apellido (en minúsculas)
         # en el caso se llama Edward y apellida agle. el login será:
         # E primera letra del nombre y se le suma el apellido Eagle

        # en el segundo caso se pasa el argumento ID que se crea con 
        # field(init=False), esto significa que no se puede inicializar 
        # directamente en el constructor. Por lo que dará error
        # TypeError: __init__() got an unexpected keyword argument 'id'
