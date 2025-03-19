import sys
import antigravity

def geohashing(latitude, longitude, datedow):
    """
    Calcula el geohash usando la función antigravity.geohash.
    Abre el resultado en el navegador.

    Parámetros:
        latitude (float): Latitud de la ubicación.
        longitude (float): Longitud de la ubicación.
        datedow (str): Fecha y valor decimal en formato "YYYY-MM-DD-decimal".
    """
    try:
        # Codifica el tercer parámetro (datedow) a bytes en formato UTF-8
        encoded_datedow = datedow.encode('utf-8')

        # Llama a la función antigravity.geohash con los parámetros correctos
        antigravity.geohash(float(latitude), float(longitude), encoded_datedow)
    except ValueError:
        print("Error: La latitud y longitud deben ser números válidos.")
        sys.exit(1)
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        sys.exit(1)

def main():
    """
    Función principal que gestiona los argumentos y ejecuta el cálculo del geohash.
    """
    if len(sys.argv) != 4:
        print("Error: Número incorrecto de argumentos.")
        print("Uso: python geohashing.py <latitud> <longitud> <fecha-dow>")
        sys.exit(1)

    # Extrae los argumentos de la línea de comandos
    latitude = sys.argv[1]
    longitude = sys.argv[2]
    datedow = sys.argv[3]

    # Llama a la función geohashing con los parámetros proporcionados
    geohashing(latitude, longitude, datedow)

if __name__ == '__main__':
    main()



# py geohashing.py 37.421542 -122.085589 2005-05-26-10458.68


"""
Función antigravity.geohash():

Esta función es una especie de "huevo de pascua" (easter egg) dentro del módulo 
antigravity de Python.

No implementa el algoritmo de geohashing como tal.

En su lugar, simplemente abre el cómic de xkcd número 353 en un navegador web.

¿Por qué lleva a xkcd.com/353?:

El cómic xkcd 353 está relacionado con el concepto de geohashing. Puedes verlo en
 https://xkcd.com/353/.

Comportamiento esperado:

Cuando llamas a antigravity.geohash(), Python abre una ventana de navegador que
muestra ese cómic en particular.
"""