# Clase base para bebidas calientes
class HotBeverage:
    price = 0.30
    name = "hot beverage"

    def description(self):
        # Descripción por defecto para bebidas calientes
        return "Just some hot water in a cup."

    def __str__(self):
        # Formato de presentación para todas las bebidas
        return (f"name : {self.name}\n"
                f"price : {self.price:.2f}\n"
                f"description : {self.description()}")

# Clase para café, hereda de HotBeverage
class Coffee(HotBeverage):
    name = "coffee"
    price = 0.40

    def description(self):
        # Descripción específica para café
        return "A coffee, to stay awake."

# Clase para té, hereda de HotBeverage
class Tea(HotBeverage):
    name = "tea"
    # No es necesario redefinir price ni description, ya que son iguales a la 
    # clase padre

# Clase para chocolate, hereda de HotBeverage
class Chocolate(HotBeverage):
    name = "chocolate"
    price = 0.50

    def description(self):
        # Descripción específica para chocolate
        return "Chocolate, sweet chocolate..."

# Clase para cappuccino, hereda de HotBeverage
class Cappuccino(HotBeverage):
    name = "cappuccino"
    price = 0.45

    def description(self):
        # Descripción específica para cappuccino
        return "Un po' di Italia nella sua tazza!"

# Pruebas
if __name__ == "__main__":
    # Crear una lista con una instancia de cada tipo de bebida
    beverages = [HotBeverage(), Coffee(), Tea(), Chocolate(), Cappuccino()]
    
    # Imprimir la información de cada bebida
    for beverage in beverages:
        print(beverage)
        print()  # Línea en blanco para separar las bebidas