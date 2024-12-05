import random
import string
from dataclasses import dataclass, field


def generate_random_id() -> str:
    """
    Generates a random student ID of 15 characters consisting of
    lowercase letters and digits.

    Returns:
        str: A randomly generated student ID.
    """
    return ''.join(
        random.choices(string.ascii_lowercase + string.digits, k=15)
    )


@dataclass
class Student:
    """
    Represents a student with their first name, last name, active status,
    login, and a unique ID.

    Attributes:
        name (str): The student's first name.
        surname (str): The student's last name.
        active (bool): Indicates whether the student is active (defaults to
         True).
        login (str): The student's login, generated from their first and
        last name.
        id (str): A unique identifier for the student, generated automatically.
    """

    name: str
    surname: str
    active: bool = False  # Student's active status
    login: str = field(init=False)  # Automatically generated login
    id: str = field(init=False, default_factory=generate_random_id)

    def __post_init__(self):
        """
        Automatically generates the student's login based on their first name
        and last name. The login format is the first letter of the first name
        followed by the surname in lowercase.
        """
        self.login = f"{self.name[0].upper()}{self.surname.lower()}"
