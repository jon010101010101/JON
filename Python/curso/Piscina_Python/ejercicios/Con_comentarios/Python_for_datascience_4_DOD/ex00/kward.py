El uso de **kwargs en Python permite que una función acepte un número variable
 de argumentos con nombre (keyword arguments). Esto es útil cuando no se 
 conoce de antemano cuántos argumentos se pasarán a la función o si se desea
  proporcionar una interfaz flexible.
¿Qué son *args y **kwargs?

    *args: Permite pasar un número variable de argumentos posicionales a una
     función. 
    Estos argumentos se almacenan como una tupla dentro de la función.
    **kwargs: Permite pasar un número variable de argumentos con nombre a una
     función. 
    Estos argumentos se almacenan como un diccionario dentro de la función,
     donde las claves son los nombres de los argumentos y los valores son 
     los valores correspondientes.

Ejemplo de Uso
Aquí hay un ejemplo sencillo que ilustra cómo funcionan *args y **kwargs:

python
def example_function(*args, **kwargs):
    """Prints positional and keyword arguments."""
    print("Positional arguments (args):")
    for arg in args:
        print(arg)
    
    print("\nKeyword arguments (kwargs):")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Llamada a la función con varios argumentos
example_function(1, 2, 3, name="Alice", age=30)

Salida Esperada
Cuando ejecutas el código anterior, obtendrás la siguiente salida:

text
Positional arguments (args):
1
2
3

Keyword arguments (kwargs):
name: Alice
age: 30
