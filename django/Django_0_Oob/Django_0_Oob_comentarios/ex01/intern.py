# Clase para representar un café
class Coffee:
    def __str__(self):
        # Método que devuelve una descripción del café
        return "This is the worst coffee you ever tasted."

# Clase para representar un pasante
class Intern:
    def __init__(self, name="My name? I'm nobody, an intern, I have no name."):
        # Constructor que inicializa el nombre del pasante
        self.Name = name

    def __str__(self):
        # Método que devuelve el nombre del pasante
        return self.Name

    def work(self):
        # Método que simula el trabajo del pasante, lanzando una excepción
        raise Exception("I'm just an intern, I can't do that...")

    def make_coffee(self):
        # Método que crea y devuelve una instancia de la clase Coffee
        return Coffee()

# Pruebas
if __name__ == "__main__":
    # Instanciar dos veces la clase Intern
    intern1 = Intern()  # Sin nombre
    intern2 = Intern("Mark")  # Con nombre "Mark"

    # Mostrar el nombre de cada instancia
    print(intern1)
    print(intern2)

    # Pedir a Mark que haga café y mostrar el resultado
    try:
        coffee = intern2.make_coffee()
        print(coffee)
    except Exception as e:
        # Manejo de posibles errores al hacer café
        print(f"Error al hacer café: {e}")

    # Pedir al otro pasante que trabaje y manejar la excepción
    try:
        intern1.work()
    except Exception as e:
        # Captura y muestra el error cuando el pasante intenta trabajar
        print(f"Error: {e}")



"""
RESPUESTA
My name? I'm nobody, an intern, I have no name.
Mark
This is the worst coffee you ever tasted.
Error: I'm just an intern, I can't do that...

"My name? I'm nobody, an intern, I have no name." - Este es el nombre del primer 
pasante (intern1), que usa el valor por defecto.

"Mark" - Este es el nombre del segundo pasante (intern2).

"This is the worst coffee you ever tasted." - Este es el resultado de pedirle a 
Mark (intern2) que haga café.

"Error: I'm just an intern, I can't do that..." - Este es el mensaje de error que
 se obtiene al pedirle al primer pasante (intern1) que trabaje.
"""