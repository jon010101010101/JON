# Markdown

This file is written in **Markdown**.

## Package Description

    Package Name: ft_package
    Version: 0.0.1
    Main Function: count_in_list


Function count_in_list

La función count_in_list toma dos argumentos:

    lst: Una lista de elementos (puede ser una lista de cadenas, números, etc.).
    item: El elemento que quieres contar en la lista.

La función devuelve un entero que indica cuántas veces aparece el item en la lista lst.

## Pasos para el Funcionamiento
**Paso 1: Asegúrate de tener todos los archivos necesarios**

Antes de comenzar, asegúrate de que los archivos esenciales para tu paquete estén en la estructura correcta. Los archivos clave que necesitas tener son:

    setup.py: Define los metadatos del paquete.
    LICENSE: Archivo de licencia.
    README.md o README.txt: Archivo de información del paquete.
    pyproject.toml: Contiene la configuración para construir el paquete.
f   t_package/: Carpeta del paquete que contiene al menos dos archivos:
    __init__.py: Archivo que hace que el directorio sea un paquete Python.
    count.py: Archivo que contiene la función count_in_list.

**Paso 2: Verifica la estructura del directorio**
 Asegúrate de que la estructura de tu directorio se parezca a la siguiente: ex09/
├── LICENSE
├── README.md
├── setup.py
├── pyproject.toml
└── ft_package
├── init.py
└── count.py 

El resto de directorios y archivos necesarios se generarán automáticamente. 

**Paso 3: Construye el paquete**
 Para construir el paquete en formato .whl y .tar.gz, ejecuta el siguiente comando desde el directorio raíz de tu proyecto, donde se encuentra setup.py: python3 setup.py sdist bdist_wheel Esto generará los archivos en el directorio dist/:

    ft_package-0.0.1-py3-none-any.whl
    ft_package-0.0.1.tar.gz

## Paso 4: Instala el paquete
 **Opción 1: Instalar el archivo .whl**
 Si quieres instalar el paquete usando el archivo .whl generado, ejecuta el siguiente comando: 
 
 *pip install ./dist/ft_package-0.0.1-py3-none-any.whl*

 **Opción 2: Instalar el archivo .tar.gz**
 Si prefieres usar el archivo fuente .tar.gz, puedes instalar el paquete con este comando: 
 
 *pip install ./dist/ft_package-0.0.1.tar.gz*
 
 ## Paso 5: Verifica la instalación
 Después de instalar el paquete, puedes verificar si se instaló correctamente ejecutando: 
 
 *pip list*
 
 Aparecerá una larga lista de los paquetes que tienes instalados. Deberías ver ft_package en la lista de paquetes instalados. También puedes obtener información más detallada sobre el paquete con: 
 
 *pip show -v ft_package*
 Aparecen los detalles de ft-package: Name: ft-package
    Version: 0.0.1
    Summary: A sample test package
    Home-page: UNKNOWN
    Author: eagle
    Author-email: eagle@42.fr
    License: MIT
    Location: /home/jurrutia/.local/lib/python3.10/site-packages
    Requires:
    Required-by:
    Metadata-Version: 2.1
    Installer: pip
    Classifiers:
    Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent
    Entry-points: 

## Paso 6: Ejecuta el script de prueba
Crea un archivo llamado test_script.py y copia el siguiente código: from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto")) # salida: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # salida: 0 

Finalmente, para probar si el paquete y su función count_in_list funcionan correctamente, ejecuta el script test_script.py: 

*python3 test_script.py*

Deberías ver la siguiente salida: 2 0 """

## archivo pyproject.toml
[build-system]: Esta sección define el sistema de construcción que se utilizará para empaquetar tu proyecto. [requires]: Esta línea especifica las dependencias necesarias para construir el paquete. En este caso:

    setuptools>=42: Indica que necesitas al menos la versión 42 de 
    setuptools. setuptools es una biblioteca que facilita la creación 
    de paquetes Python. Esta versión mínima asegura que tengas 
    acceso a las características y mejoras introducidas en 
    versiones posteriores.

    wheel: Esta es otra biblioteca que permite crear paquetes Python
    en formato "wheel", que es un formato de distribución binaria. Los 
    archivos .whl son más fáciles y rápidos de instalar que los archivos 
    de distribución de fuentes, ya que no requieren compilar el 
    código.


[[build-backend] Aquí especificas qué backend se utilizará para la construcción del paquete. En tu caso, setuptools.build_meta es un backend que permite a setuptools manejar la construcción del paquete según los metadatos que has proporcionado. Es una opción comúnmente utilizada, ya que setuptools es una de las herramientas más populares para crear paquetes en Python.

## archivo dist
[Wheels]: Archivos con extensión .whl que son el formato de distribución binaria más comúnmente utilizado en Python. Estos archivos son fáciles y rápidos de instalar, ya que contienen el código precompilado y la información necesaria para hacer la instalación sencilla. Por ejemplo, en tu salida de ls, tenemos ft_package-0.0.1-py3-none-any.whl. [Archivos TAR.GZ]: Archivos con extensión .tar.gz son distribuciones de fuentes. Contienen el código fuente del paquete y generalmente necesitan ser compilados o instalados desde cero cuando se utilizan. En este caso, tenemos ft_package-0.0.1.tar.gz. Para qué sirven: Los archivos en el directorio dist se utilizan para distribuir tu paquete. Cuando alguien quiere instalar tu paquete, generalmente lo hace desde un archivo en este directorio.

## directorio ./ft_package.egg-info

El directorio ./ft_package.egg-info es creado automáticamente por setuptools cuando construyes tu paquete. Este directorio contiene metadatos sobre tu paquete y es parte del sistema de empaquetado de Python. Aquí tienes una breve descripción de los archivos que mencionaste:

    dependency_links.txt: Este archivo puede listar enlaces a dependencias que no están disponibles en el Python Package Index (PyPI). Aunque su uso es raro hoy en día, algunas configuraciones más antiguas pueden requerirlo aún.

    PKG-INFO: Contiene metadatos importantes sobre tu paquete, como su nombre, versión, autor, dirección de correo electrónico del autor, descripción y licencia. Es esencial para la instalación y distribución.

    SOURCES.txt: Lista todos los archivos fuente incluidos en el paquete. Ayuda a los instaladores a saber qué archivos necesitan ser instalados.

    top_level.txt: Enumera los módulos de nivel superior del paquete, incluyendo el nombre del paquete y cualquier submódulo considerado como módulo de nivel superior.


TEstos archivos son generados automáticamente por setuptools y proporcionan información útil para gestionar dependencias y facilitar la instalación de tu paquete.

## Directorio ./build
El directorio ./build también es creado automáticamente por setuptools cuando construyes tu paquete. Este directorio se utiliza durante el proceso de construcción para contener archivos temporales y los archivos de distribución construidos. Aquí tienes una breve descripción de lo que ves en el directorio ./build:

    bdist.linux-x86_64: Este subdirectorio se crea para contener la distribución construida para la plataforma específica (en este caso, Linux x86_64). Típicamente contendrá los archivos de distribución binaria que están listos para ser instalados.

    lib: Este subdirectorio contiene los archivos de biblioteca del paquete, incluyendo el código fuente de tu paquete. El directorio ft_package dentro de lib contiene los archivos reales del paquete, como __init__.py y count.py, que definiste en tu paquete.
