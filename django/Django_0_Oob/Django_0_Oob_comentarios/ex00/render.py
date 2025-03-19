import os  # Importa el módulo para operaciones del sistema operativo
import sys  # Importa el módulo para funciones y parámetros específicos del sistema

EXTENSION = ".template"  # Define la extensión de los archivos de plantilla
SETTINGS_FILENAME = "settings.py"  # Define el nombre del archivo de configuración

def read_file(file_path):
    """
    Lee el contenido de un archivo.

    Args:
    file_path (str): Ruta del archivo a leer.

    Returns:
    str: Contenido del archivo.

    Raises:
    SystemExit: Si ocurre algún error durante la lectura.
    """
    try:
        with open(file_path, 'r') as file:  # Abre el archivo en modo lectura
            return file.read()  # Lee y retorna el contenido del archivo
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")  # Maneja error si el archivo no existe
    except PermissionError:
        print(f"Error: No permission to read {file_path}")  # Maneja error de permisos
    except IsADirectoryError:
        print(f"Error: {file_path} is a directory")  # Maneja error si es un directorio
    except Exception as e:
        print(f"Error: {e}")  # Maneja cualquier otro error
    sys.exit(1)  # Sale del programa con código de error

def parse_settings(file_path):
    """
    Parsea el archivo de configuración.

    Args:
    file_path (str): Ruta del archivo de configuración.

    Returns:
    dict: Diccionario con los parámetros de configuración.

    Raises:
    SystemExit: Si hay un error en el formato del archivo.
    """
    content = read_file(file_path)  # Lee el contenido del archivo
    param_dict = {}  # Inicializa el diccionario para almacenar los parámetros
    for line in content.splitlines():  # Itera sobre cada línea del contenido. 
            # content.splitlines()  metodo que ddivide el texto content en una lista de 
            # subcadenas, utilizando los saltos de linea como separadores
        line = line.strip()  # Elimina espacios en blanco al inicio y final
        if line and not line.startswith('#'):  # Ignora líneas vacías (line) y comentarios 
            # con line.startswith('#')
            try:
                key, value = line.split('=', 1)  # Divide la línea en clave y valor signo = y 1
                # key recibe el primer elemento de la lista resultante (la parte antes del '=').
                # value recibe el segundo elemento (la parte después del '=')
                param_dict[key.strip()] = value.strip().strip('"\'')  # Almacena en el diccionario
            except ValueError:
                print(f"Error: Invalid line in settings file: {line}")  # Maneja error de formato
                sys.exit(1)  # Sale del programa con código de error
    return param_dict  # Retorna el diccionario de parámetros

def render_template(template_path, param_dict):
    """
    Renderiza la plantilla con los parámetros dados.

    Args:
    template_path (str): Ruta del archivo de plantilla.
    param_dict (dict): Diccionario con los parámetros de configuración.

    Raises:
    SystemExit: Si hay un error al escribir el archivo de salida.
    """
    content = read_file(template_path)  # Lee el contenido de la plantilla
    rendered = content.format(**param_dict)  # Renderiza la plantilla con los parámetros
    
    output_path = os.path.splitext(template_path)[0] + '.html'  # Genera la ruta del archivo de salida
    try:
        with open(output_path, 'w') as f:  # Abre el archivo de salida en modo escritura
            f.write(rendered)  # Escribe el contenido renderizado. f es la variaable del objeto
        print(f"HTML file created: {output_path}")  # Informa que se ha creado el archivo
    except Exception as e:
        print(f"Error writing output file: {e}")  # Maneja error de escritura
        sys.exit(1)  # Sale del programa con código de error

def main():
    """
    Función principal del programa.

    Raises:
    SystemExit: Si hay errores en los argumentos o archivos.
    """
    if len(sys.argv) != 2:  # Verifica que se proporcione exactamente un argumento
        print(f"Usage: python {sys.argv[0]} <file.template>")  # Muestra el uso correcto
        sys.exit(1)  # Sale del programa con código de error

    template_path = sys.argv[1]  # Obtiene la ruta de la plantilla del argumento
    if not template_path.endswith(EXTENSION):  # Verifica la extensión del archivo
        print(f"Error: File must have {EXTENSION} extension")  # Muestra error si la extensión es incorrecta
        # f es una string de Python que permitee inscrustar expresiones dentro de cadenass de uso.
        # file template es un marcador que indica que debe proporcionar un archivo .template
        sys.exit(1)  # Sale del programa con código de error

    if not os.path.exists(template_path):  # Verifica si existe el archivo de plantilla
        print(f"Error: {template_path} does not exist")  # Muestra error si no existe
        sys.exit(1)  # Sale del programa con código de error

    if not os.path.exists(SETTINGS_FILENAME):  # Verifica si existe el archivo de configuración
        print(f"Error: {SETTINGS_FILENAME} not found")  # Muestra error si no existe
        sys.exit(1)  # Sale del programa con código de error

    param_dict = parse_settings(SETTINGS_FILENAME)  # Parsea el archivo de configuración
        # lee el archivo linea por linea, ignora las vacias y comentarios (enpiecen por #) 
        # y divide cada linea en una clave y valor usando el signo = como separador
    render_template(template_path, param_dict)  # Renderiza la plantilla. Significa procesar
    # una plantilla HTML y generar el documento HTML final. param_dict = {"nombre": "Juan"}, 
    # el resultado renderizado reemplazará {{ nombre }} con "Juan" en el HTML final

if __name__ == "__main__":
    main()  # Ejecuta la función principal si el script se ejecuta directamente






# python3 render.py myCV.template

# MANEJO DE ERRORES
# Error 1: Si el archivo .template no existe:
# Error: myCV.template no existe

# Error 2: Si falta una variable en settings.py:
# Variable faltante en settings.py: 'nombre'

# Error 3: Si se usan argumentos incorrectos:
# Error: Uso: python render.py archivo.template
