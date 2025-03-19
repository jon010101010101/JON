# Importamos el módulo random y las clases de bebidas del archivo beverages.py
import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

# Clase CoffeeMachine que representa una máquina expendedora de bebidas calientes
class CoffeeMachine:
    # Clase interna EmptyCup que hereda de HotBeverage
    class EmptyCup(HotBeverage):
        def __init__(self):
            # Inicializa el nombre y precio de la taza vacía
            self.name = "empty cup"
            self.price = 0.90

        def description(self):
            # Devuelve la descripción de la taza vacía
            return "An empty cup?! Gimme my money back!"

    # Clase personalizada para la excepción de máquina rota
    class BrokenMachineException(Exception):
        def __init__(self):
            # Inicializa el mensaje de error para la excepción
            super().__init__("This coffee machine has to be repaired.")

    def __init__(self):
        # Constructor que inicializa el contador de bebidas servidas
        self.served_drinks = 0

    def repair(self):
        # Método que reinicia el contador de bebidas servidas para reparar la máquina
        self.served_drinks = 0

    def serve(self, beverage_class):
        # Método que sirve una bebida, alternando entre la solicitada y una taza vacía
        if self.served_drinks >= 10:
            # Si se han servido 10 bebidas, lanza una excepción de máquina rota
            raise self.BrokenMachineException()
        
        # Incrementa el contador de bebidas servidas
        self.served_drinks += 1
        # Devuelve aleatoriamente una instancia de la bebida solicitada o una taza vacía
        return random.choices([beverage_class(), self.EmptyCup()], weights=[0.75, 0.25])[0]
        # [0] Hay que ponerle esto por que si no entiende que es una lista que contiene un 
        # objeto (capuccino), no el objeto Cappuccino directamente

# Pruebas
if __name__ == "__main__":
    # Crea una instancia de la máquina expendedora
    machine = CoffeeMachine()
    
    # Lista de clases de bebidas para probar
    beverages = [Coffee, Tea, Chocolate, Cappuccino, HotBeverage]

    # Inicializa las estadísticas y contadores
    stats = {"empty cup": 0, "coffee": 0, "tea": 0, "chocolate": 0, "cappuccino": 0, "hot beverage": 0}
    total_served = 0
    max_served = 15
    repairs = 0

    # Bucle para probar la máquina con un límite de bebidas
    while total_served < max_served:
        # Selecciona aleatoriamente una bebida de la lista
        beverage = random.choice(beverages)
        try:
            # Intenta servir la bebida seleccionada
            served = machine.serve(beverage)
            # Imprime la bebida servida
            print(f"Served: {served}")
            print()
            # Actualiza las estadísticas
            stats[served.name] += 1
            total_served += 1
        except machine.BrokenMachineException as e:
            # Maneja la excepción de máquina rota
            print(f"Error: {e}")
            print("Repairing the machine...")
            # Repara la máquina
            machine.repair()
            repairs += 1
            print("Machine repaired. Continuing...")
            print()  # Añade una línea en blanco después de reparar la máquina

    # Imprime el resumen de la prueba
    print("\nTest finished.")
    print(f"Total drinks served: {total_served}")
    print(f"Number of repairs: {repairs}")
    print("\nStatistics:")
    for key, value in stats.items():
        print(f"{key}: served {value} times")

