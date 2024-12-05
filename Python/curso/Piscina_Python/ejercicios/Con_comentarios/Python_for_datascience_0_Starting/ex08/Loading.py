# La función debe copiar la función tqdm con el operador yield

import sys
import time

"""
Definición de ft_tqdm:

    La función toma un rango como argumento y utiliza un bucle for para
    iterar sobre los elementos. Esta función no devuelve nada (None).

    Se utiliza enumerate para obtener tanto el índice (i) como el elemento (elem).
    Calculamos el porcentaje completado y construimos una barra de progreso visual.
    Usamos sys.stdout.write y sys.stdout.flush para actualizar la misma línea
    en la consola y mostrar el progreso.
"""


def ft_tqdm(lst: range) -> None:
    # Comprueba que lst es un objeto iterable
    if not isinstance(lst, range):
        raise TypeError("El argumento debe ser de tipo range.")

    total = len(lst)  # Calcula el número total de elementos en lst
    for i, elem in enumerate(lst):  # Usa enumerate para iterar
        # sobre lst, obteniendo tanto el índice i (que comienza en 0)
        # como el elemento elem en cada iteración.
        yield elem  # Usa yield para devolver el elemento actual
        percent = (i + 1) / total * 100  # Calcula el porcentaje
        # completado dividiendo el índice actual (más 1) por el total
        # de elementos y multiplicando por 100.
        bar_length = 40  # Longitud de la barra de progreso
        block = int(bar_length * percent // 100)  # Calcula cuántos
        # bloques de la barra deben mostrarse basándose en el porcentaje
        # completado. El resultado se convierte a entero.
        bar = '█' * block + '-' * (bar_length - block)  # Crea la barra
        # concatenando bloques llenos ('█') y bloques vacíos
        # ('-'). El número de bloques llenos es igual a block, mientras
        # que el número de bloques vacíos es igual a la longitud total
        # de la barra menos block.

        # Muestra el progreso
        sys.stdout.write(
            f'\r{int(percent)}%|{bar:<{bar_length}}| {i + 1}/{total}'
        )

        # Imprime el progreso en la misma línea usando \r para
        # sobrescribir la línea anterior. Muestra el porcentaje
        # completado, la barra de progreso y cuántos elementos se han
        # procesado hasta ahora.
        sys.stdout.flush()
        # Asegura que el contenido se muestre inmediatamente.
        time.sleep(0.005)  # Simula tiempo de trabajo

    print()  # Nueva línea al final

    # yield se usa en funciones para convertirlas en generadores
