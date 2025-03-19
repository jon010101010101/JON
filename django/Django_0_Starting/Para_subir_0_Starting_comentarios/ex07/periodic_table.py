import os

def parse_periodic_table(file_path):
    """Parse the periodic_table.txt file and return the element data."""
    # Inicializar una lista vacía para almacenar los elementos
    elements = []
    # Abrir el archivo en modo lectura
    with open(file_path, 'r') as file:
        # Iterar sobre cada línea del archivo
        for line in file:
            # Verificar si la línea no está vacía después de quitar espacios
            if line.strip():
                # Dividir la línea en nombre y atributos
                data = line.strip().split(' = ')
                # Obtener el nombre del elemento
                name = data[0].strip()
                # Crear un diccionario con los atributos del elemento
                attributes = dict(item.split(':') for item in data[1].split(', '))
                
                # Obtener la posición (columna) del elemento, convertir a entero
                column = int(attributes.get('position', '0'))
                # Obtener el número atómico del elemento, convertir a entero
                atomic_number = int(attributes.get('number', '0'))

                # Determinar la fila del elemento basado en su número atómico
                if atomic_number <= 2:
                    row = 1
                elif atomic_number <= 10:
                    row = 2
                elif atomic_number <= 18:
                    row = 3
                elif atomic_number <= 36:
                    row = 4
                elif atomic_number <= 54:
                    row = 5
                elif atomic_number <= 86:
                    row = 6
                else:
                    row = 7

                # Crear un diccionario con la información del elemento
                element = {
                    "name": name,
                    "atomic_number": atomic_number,
                    "symbol": attributes.get('small', ''),
                    "atomic_mass": attributes.get('molar', ''), # ' ' valor por defecto
                    "electron": attributes.get('electron', ''),
                    "position": (row, column) # Define la fila y columna
                }
                # Añadir el elemento a la lista de elementos
                elements.append(element)
    # Devolver la lista completa de elementos
    return elements

def generate_html(elements, output_file):
    """Generate an HTML file representing the periodic table."""
    # Iniciar el contenido HTML con la estructura básica y estilos CSS
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Periodic Table</title>
        <style>
            table { border-collapse: collapse; width: auto; }
            td { border: 1px solid black; padding: 10px; text-align: center; vertical-align: top; width: 80px; height: 80px; }
            h4 { margin: 0; }
            ul { padding-left: 20px; margin: 5px; list-style-type: none; }
            .empty { background-color: lightgray; }
        </style>
    </head>
    <body>
        <h1>Periodic Table of Elements</h1>
        <table>
    """
    # Viene por la tupla definida al crear el diccionario "position": (row, column),
    # posicion 0 fila y posicion 1 columna
    # Determinar el número máximo de filas en la tabla.
    max_row = max(element["position"][0] for element in elements)
    # Determinar el número máximo de columnas en la tabla
    max_column = max(element["position"][1] for element in elements)

    # Iterar sobre cada fila de la tabla, crea un bucle desde 1 hasta max fila
    for row in range(1, max_row + 1):
        # Añade una etiqueta HTML para iniciar una nueva fila de la tabla.
        html_content += "<tr>\n"
        # Iterar sobre cada columna de la fila, crea bucle desde 0 hasta max columnas
        for column in range(0, max_column + 1):
            # Buscar si hay un elemento en esta posición específica. Next es una expresion 
            # generadora que hace que busque en la lista elements el primer elemento cuya 
            # posición coincide con la fila y columna actuales.Si encuentra un elemento, 
            # lo asigna a element. Si no, asigna None.
            element = next((el for el in elements if el["position"] == (row, column)), None)
            # Si se encuentra un elemento en esta posición
            if element:
                # Añadir una celda con la información del elemento
                html_content += f"""
                <td>
                    <h4>{element['name']}</h4>
                    <ul>
                        <li>No {element['atomic_number']}</li>
                        <li>{element['symbol']}</li>
                        <li>{element['atomic_mass']}</li>
                        <li>{element['electron']} electrons</li>
                    </ul>
                </td>
                """
            else:
                # Si no hay elemento, añadir una celda vacía
                html_content += '<td class="empty"></td>\n'
        # Cerrar la fila HTML
        html_content += "</tr>\n"

    # Cerrar la estructura HTML
    html_content += """
        </table>
    </body>
    </html>
    """

    # Escribir el contenido HTML en el archivo de salida
    with open(output_file, 'w') as file:
        file.write(html_content)

def main():
    # Obtener la ruta del directorio del script actual. 
    # os.path.abspath(__file__): Convierte la ruta relativa de __file__ en una ruta absoluta
    # os.path.dirname(path): Extrae el nombre del directorio de una ruta completa.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construir la ruta completa del archivo de entrada
    input_file = os.path.join(script_dir, "periodic_table.txt")
    # Construir la ruta completa del archivo de salida
    output_file = os.path.join(script_dir, "periodic_table.html")

    # Imprimir un mensaje indicando el intento de abrir el archivo
    print(f"Attempting to open file: {input_file}")

    # Verificar si el archivo de entrada existe
    if not os.path.exists(input_file):
        # Si no existe, imprimir un mensaje de error y terminar la función
        print(f"Error: Input file '{input_file}' not found.")
        return

    try:
        # Analizar el archivo de entrada para obtener los datos de los elementos
        elements = parse_periodic_table(input_file)
        # Generar el archivo HTML con la tabla periódica
        generate_html(elements, output_file)
        # Imprimir un mensaje de éxito
        print(f"Periodic table generated in HTML: {output_file}")
    except Exception as e:
        # Si ocurre algún error, imprimir el mensaje de error
        print(f"Error processing file: {e}")
        # Importar el módulo traceback para obtener más detalles del error
        import traceback
        # Imprimir el traceback completo del error
        print(traceback.format_exc())

# Verificar si este script se está ejecutando directamente
if __name__ == "__main__":
    # Si es así, llamar a la función main
    main()




#  COMENTARIOS

# Disponer los elementos en líneas y columnas (también denominados "períodos" y 
# "grupos") dentro de un rectángulo, con sus pesos atómicos en orden ascendente 
# de Izquierda a derecha dentro de la misma línea hasta bajar a la segunda y así 
# sucesivamente.

# La tabla periodica se ordena en 7 filas y 18 columnas, las filas vienen definidas por el
#  numero atomico (number en la base de datos)

#Fila 1: Z = 1-2
#Fila 2: Z = 3-10
#Fila 3: Z = 11-18
#Fila 4: Z = 19-36
#Fila 5: Z = 37-54
#Fila 6: Z = 55-86
#Fila 7: Z = 87-118

# Las coumnas vienen definidas por position + 1 en la base de datos (hay que sumarle uno, 
# por que hayy position 0)

