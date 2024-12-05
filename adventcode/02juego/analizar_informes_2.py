def es_informe_seguro(informe):
    """
    Verifica si un informe es seguro según las reglas:
    - Todos los números deben aumentar o disminuir de forma continua.
    - Las diferencias entre números consecutivos deben estar entre 1 y 3.
    """
    diferencias = [informe[i + 1] - informe[i] for i in range(len(informe) - 1)]
    if all(1 <= diferencia <= 3 for diferencia in diferencias):  # Aumento gradual
        return True
    if all(-3 <= diferencia <= -1 for diferencia in diferencias):  # Disminución gradual
        return True
    return False

def puede_ser_seguro_con_una_remocion(informe):
    """
    Verifica si un informe puede ser seguro al eliminar un solo nivel.
    """
    for i in range(len(informe)):
        informe_modificado = informe[:i] + informe[i+1:]
        if es_informe_seguro(informe_modificado):
            return True
    return False

def contar_informes_seguros(nombre_archivo):
    """
    Cuenta la cantidad de informes seguros en un archivo de texto, considerando el problema Dampener.
    """
    informes_seguros = 0
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                informe = list(map(int, linea.split()))
                # Comprobar si el informe es seguro o si puede ser seguro al eliminar un nivel
                if es_informe_seguro(informe) or puede_ser_seguro_con_una_remocion(informe):
                    informes_seguros += 1
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{nombre_archivo}'.")
    except ValueError:
        print(f"Error: Formato incorrecto en el archivo '{nombre_archivo}'.")
    return informes_seguros

# Nombre del archivo de datos
nombre_archivo = "input02juego2"

# Contar informes seguros
informes_seguros = contar_informes_seguros(nombre_archivo)
print(f"Cantidad de informes seguros: {informes_seguros}")
