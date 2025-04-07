#!/bin/bash

# Mostrar la versión de pip
echo "Versión de pip:"
python -m pip --version

# Definir el directorio local_lib
LIB_DIR="./local_lib"

# Eliminar el directorio local_lib si existe
if [ -d "$LIB_DIR" ]; then
    echo "Eliminando el directorio local_lib existente..."
    rm -rf "$LIB_DIR"
fi

# Crear el directorio local_lib
mkdir -p "$LIB_DIR"

# Instalar la versión de desarrollo de path.py desde GitHub en local_lib
echo "Instalando path.py..."
pip install --upgrade git+https://github.com/jaraco/path.py.git -t "$LIB_DIR" > path_install.log 2>&1

# Verificar si la instalación fue exitosa
# $? es una variable especial en Bash que contiene el código de salida del último comando ejecutado
# -eq es un operador de comparación numérica en Bash que significa "igual a".
# [ $? -eq 0 ] comprueba si el código de salida del último comando es igual a 0.
# then es una palabra clave en Bash que se usa después de la condición en una declaración if.
if [ $? -eq 0 ]; then
    echo "path.py instalado correctamente."
    # Ejecutar el programa Python con PYTHONPATH
    PYTHONPATH="$LIB_DIR" python my_program.py
else
    echo "Error al instalar path.py. Revisa path_install.log para más detalles."
fi


# ./my_script.sh
# cat my_folder/my_file.txt




# Bash (Bourne-Again Shell) es un intérprete de comandos y lenguaje de scripting 
# ampliamente utilizado en sistemas Unix y Linux.
# Sus principales características son:
# 
# Interfaz de línea de comandos: Permite a los usuarios interactuar directamente con 
# el sistema operativo mediante comandos de texto.
# Lenguaje de scripting: Facilita la creación de scripts para automatizar tareas 
# repetitivas y complejas.
# Gestión de procesos: Permite iniciar, detener y manipular procesos en ejecución.
# Redirección y piping: Posibilita redirigir la entrada/salida de comandos y conectar
# múltiples comandos.
# Variables y control de flujo: Soporta el uso de variables, bucles y condicionales 
# para crear scripts dinámicos y flexibles.
# Personalización del entorno: Permite a los usuarios personalizar su entorno de 
# shell mediante archivos de configuración.
# Compatibilidad: Diseñado como una mejora del Bourne Shell original, mantiene 
# compatibilidad con scripts sh.
# 
# Bash es esencial para desarrolladores y administradores de sistemas que trabajan 
# en entornos Unix/Linux, ya que proporciona un control granular sobre el sistema 
# operativo y facilita la automatización de tareas complejas.
