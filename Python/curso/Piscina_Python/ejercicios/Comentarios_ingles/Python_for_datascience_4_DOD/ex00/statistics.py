from typing import Any, List
from math import sqrt


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calcula diversas medidas estadísticas basadas en los argumentos
    numéricos proporcionados.

    Esta función acepta un número arbitrario de argumentos numéricos y
    calcula la media, mediana, cuartiles (25% y 75%), desviación estándar
    y varianza según las palabras clave especificadas en kwargs. Si no se
    proporcionan números válidos o se utiliza una palabra clave no válida,
    se imprimirán mensajes de error apropiados.

    Args:
        *args: Un número variable de valores numéricos (int o float).
        **kwargs: Argumentos con nombre que especifican qué medidas
        estadísticas calcular.
                  Claves válidas incluyen:
                      - "mean": Calcular la media de los números.
                      - "median": Calcular la mediana de los números.
                      - "quartile": Calcular los primeros y terceros cuartiles.
                      - "std": Calcular la desviación estándar.
                      - "var": Calcular la varianza.

    Returns:
        None: La función imprime los resultados directamente en la salida
        estándar.
    """

    # Filtra los valores no numéricos de args
    nums: List[float] = [x for x in args if isinstance(x, (int, float))]

    # Verifica si hay números válidos para procesar
    if not nums:
        print("ERROR")
        return

    # Define funciones estadísticas
    def mean(ls: List[float]) -> float:
        """Calcula la media de una lista."""
        return sum(ls) / len(ls)

    def median(ls: List[float]) -> float:
        """Calcula la mediana de una lista."""
        sorted_ls = sorted(ls)
        mid = len(sorted_ls) // 2
        return (sorted_ls[mid]
                if len(sorted_ls) % 2 != 0
                else (sorted_ls[mid - 1] + sorted_ls[mid]) / 2)

    def var(ls: List[float]) -> float:
        """Calcula la varianza de una lista."""
        m = mean(ls)
        return mean([(x - m) ** 2 for x in ls])

    def std(ls: List[float]) -> float:
        """Calcula la desviación estándar de una lista."""
        return sqrt(var(ls))

    def quartile(ls: List[float]) -> List[float]:
        """Calcula los cuartiles de una lista."""
        s = sorted(ls)
        mid = len(s) // 2

        # Calcula Q1 y Q3 usando median
        q1 = median(s[:mid])  # Primer cuartil
        q3 = median(s[mid + (0 if len(s) % 2 == 0 else 1):])  # Tercer cuartil

        return [q1, q3]

    # Ejecuta las operaciones solicitadas
    for key, value in kwargs.items():
        if value == "mean": # media
            print(f"mean : {mean(nums)}")
        elif value == "median": #mediana
            print(f"median : {median(nums)}")
        elif value == "quartile": #quartil
            print(f"quartile : {quartile(nums)}")
        elif value == "std": #desviacion estandar
            print(f"std : {std(nums)}")
        elif value == "var": #varianza
            print(f"var : {var(nums)}")
        else:
            print("ERROR")  # Solo imprime ERROR para palabras clave inválidas


def main():
    """
    Función principal para probar ft_statistics con varios inputs
    y manejo de errores.
    """
    try:
        ft_statistics(1, 42, 360, 11, 64,
                      toto="mean", tutu="median", tata="quartile")
        print("-----")

        ft_statistics(5, 75, 450, 18, 597,
                      27474, 48575, hello="std", world="var")
        print("-----")

        ft_statistics(5, 75, 450, 18, 597,
                      27474, 48575,
                      ejfhhe="heheh", ejdjdejn="kdekem")
        print("-----")

        # No se proporcionaron valores numéricos
        ft_statistics(toto="mean", tutu="median",
                      tata="quartile")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    main()

"""
**kwargs es una sintaxis especial en Python que se utiliza en las 
definiciones de funciones para pasar una lista de argumentos de longitud
 variable con nombre (keyword arguments). Aquí tienes un desglose de lo que
  significa **kwargs y cómo se utiliza:

    Definición:
        **kwargs permite que una función acepte un número arbitrario de 
        argumentos con nombre.
        El doble asterisco ** es la parte importante; kwargs es solo una 
        convención (puedes usar cualquier nombre de variable válido).

    Recoge todos los argumentos adicionales con nombre en un diccionario.
    Las claves de este diccionario son los nombres de los argumentos, y los
     valores son los valores de esos argumentos.

    Uso en la Definición de Funciones:

    def ejemplo_funcion(**kwargs):
        for clave, valor in kwargs.items():
            print(f"{clave}: {valor}")

    Llamando a una Función con **kwargs:

    ejemplo_funcion(nombre="Alice", edad=30, ciudad="Nueva York")

    Casos de Uso Comunes:

    Crear interfaces de API flexibles.
    Implementar funciones envolventes (wrappers) o decoradores.
    Pasar opciones de configuración.

    Ejemplo Combinando *args y **kwargs:

def ejemplo_combinado(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

ejemplo_combinado(1, 2, 3, nombre="Alice", edad=30)

Desempaquetando Diccionarios:
También puedes usar ** para desempaquetar diccionarios al llamar a funciones:

def saludar(nombre, edad):
    print(f"Hola {nombre}, tienes {edad} años.")

persona = {"nombre": "Bob", "edad": 25}
saludar(**persona)




"""