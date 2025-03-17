import os

def parse_periodic_table(file_path):
    """Analiza el archivo periodic_table.txt y devuelve los datos de los elementos."""
    elementos = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Ignorar líneas vacías
                datos = line.strip().split(' = ')
                nombre = datos[0].strip()
                atributos = dict(item.split(':') for item in datos[1].split(', '))
                
                # Determinar posición en la tabla
                columna = int(atributos.get('position', '0'))
                numero_atomico = int(atributos.get('number', '0'))

                # Calcular fila basada en el número atómico
                if numero_atomico <= 2:
                    fila = 1
                elif numero_atomico <= 10:
                    fila = 2
                elif numero_atomico <= 18:
                    fila = 3
                elif numero_atomico <= 36:
                    fila = 4
                elif numero_atomico <= 54:
                    fila = 5
                elif numero_atomico <= 86:
                    fila = 6
                else:
                    fila = 7

                elemento = {
                    "nombre": nombre,
                    "numero_atomico": numero_atomico,
                    "simbolo": atributos.get('small', ''),
                    "masa_atomica": atributos.get('molar', ''),
                    "electron": atributos.get('electron', ''),
                    "posicion": (fila, columna)
                }
                elementos.append(elemento)
    return elementos

def generar_html(elementos, archivo_salida):
    """Genera un archivo HTML que representa la tabla periódica."""
    contenido_html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tabla Periódica</title>
        <style>
            table { border-collapse: collapse; width: auto; }
            td { border: 1px solid black; padding: 10px; text-align: center; vertical-align: top; width: 80px; height: 80px; }
            h4 { margin: 0; }
            ul { padding-left: 20px; margin: 5px; list-style-type: none; }
            .vacio { background-color: lightgray; }
        </style>
    </head>
    <body>
        <h1>Tabla Periódica de los Elementos</h1>
        <table>
    """

    # Determinar dimensiones de la tabla
    max_fila = max(elemento["posicion"][0] for elemento in elementos)
    max_columna = max(elemento["posicion"][1] for elemento in elementos)

    # Crear filas y columnas de la tabla
    for fila in range(1, max_fila + 1):
        contenido_html += "<tr>\n"
        for columna in range(0, max_columna + 1):
            elemento = next((el for el in elementos if el["posicion"] == (fila, columna)), None)
            if elemento:
                contenido_html += f"""
                <td>
                    <h4>{elemento['nombre']}</h4>
                    <ul>
                        <li>No {elemento['numero_atomico']}</li>
                        <li>{elemento['simbolo']}</li>
                        <li>{elemento['masa_atomica']}</li>
                        <li>{elemento['electron']} electrones</li>
                    </ul>
                </td>
                """
            else:
                contenido_html += '<td class="vacio"></td>\n'
        contenido_html += "</tr>\n"

    contenido_html += """
        </table>
    </body>
    </html>
    """

    with open(archivo_salida, 'w') as file:
        file.write(contenido_html)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    archivo_entrada = os.path.join(script_dir, "periodic_table.txt")
    archivo_salida = os.path.join(script_dir, "periodic_table.html")

    print(f"Intentando abrir el archivo: {archivo_entrada}")

    if not os.path.exists(archivo_entrada):
        print(f"Error: No se encontró el archivo de entrada '{archivo_entrada}'.")
        return

    try:
        elementos = parse_periodic_table(archivo_entrada)
        generar_html(elementos, archivo_salida)
        print(f"Tabla periódica generada en HTML: {archivo_salida}")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        import traceback
        print(traceback.format_exc())

if __name__ == "__main__":
    main()


#  COMENTARIOS

# La tabla periodica tiene 7 filas y 18 columnas, y en cada fila los elementos tienene generalmente 
# numeros atomicos consecutivos

# Disponer los elementos en líneas y columnas (también denominados "períodos" y 
# "grupos") dentro de un rectángulo, con sus pesos atómicos en orden ascendente 
# de Izquierda a derecha dentro de la misma línea hasta bajar a la segunda y así 
# sucesivamente.

# relacion numero/fila 

#Fila 1: Z = 1-2
#Fila 2: Z = 3-10
#Fila 3: Z = 11-18
#Fila 4: Z = 19-36
#Fila 5: Z = 37-54
#Fila 6: Z = 55-86
#Fila 7: Z = 87-118