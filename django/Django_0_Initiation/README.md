# EJERCICIO 00

*Para ejecutar*

chmod +x myawesomescript.sh
./myawesomescript.sh bit.ly/1O72s3U
tiene que salir https://42.fr/% 


**Elecccion del Interprete**
#!/bin/sh


**Verificar si se ha proporcionado un argumento (URL)**
if [ -z "$1" ]; then

    Inicia una estructura condicional if.
    -z es un operador que comprueba si una cadena está vacía.
    "$1" se refiere al primer argumento pasado al script.
    Si $1 está vacío (no se proporcionó ningún argumento), la condición es verdadera.

echo "Usage: $0 <bit.ly URL>" >&2
    Si no se proporcionó un argumento, muestra un mensaje de uso.
    $0 representa el nombre del script.
    >&2 redirige la salida al error estándar (stderr).
exit 1
    Termina la ejecución del script con un código de salida 1, indicando un error.
fi
    Cierra la estructura condicional if.

**Obtener la URL final después de las redirecciones**
curl: Herramienta para transferir datos usando varios protocolos.
-L: Sigue las redirecciones automáticamente.
-s: Modo silencioso, suprime la barra de progreso.
-o /dev/null: Descarta el contenido de la página.
-w %{url_effective}: Muestra la URL final después de todas las redirecciones.
"$1": Usa el primer argumento proporcionado como la URL a procesar.
-->

# EJECICIO 01

Etiqueta <h2>

    Define un encabezado de segundo nivel. Se utiliza para crear subtítulos 
    o secciones dentro del contenido principal. 
    Por ejemplo, en el currículum, se podría usar para títulos como 
    "Información Personal", "Habilidades", etc.

Etiqueta <p>
    
    Define un párrafo de texto. Es una etiqueta de tipo bloque que por defecto
    ocupa una línea completa en la página web. Se utiliza para agregar texto 
    descriptivo o explicativo.

Etiqueta <ol>
    
    Define una lista ordenada. Se utiliza para crear listas numeradas. 
    En el contexto del currículum, podría usarse para enumerar la trayectoria 
    profesional o los logros.

Etiqueta <li>
    
    Define un elemento de lista. Se usa dentro de las etiquetas <ol> o <ul> 
    para especificar cada ítem de la lista. Por ejemplo, en una lista ordenada
    de trayectoria profesional, cada puesto ocupado sería un <li>.

Etiqueta <table>
    
    Define una tabla en HTML. Se utiliza para organizar datos en filas y 
    columnas. En el currículum, podría usarse para mostrar información 
    estructurada como logros económicos.

Etiqueta <tr>
    
    Define una fila dentro de una tabla. Se usa dentro de la etiqueta <table> 
    para crear filas. Cada fila de la tabla contendrá varios elementos <td>.

Etiqueta <td>
    
    No se mencionó explícitamente, pero es importante. Define una celda dentro
    de una tabla. Se utiliza para contener el contenido de cada columna en una fila.

Estilo en línea en <p>
    
    <p style="border: 1px solid blue; padding: 10px;">
    
    Este estilo en línea agrega un borde azul sólido de 1 píxel alrededor del 
    párrafo y un relleno interno de 10 píxeles. Esto se hace para resaltar 
    visualmente el contenido del párrafo, como la educación en el currículum. 

Declaración del tipo de documento:

<!DOCTYPE html>
Esto indica que el documento es HTML5.

Elemento raíz HTML:
<html lang="es">
Define el inicio del documento HTML y especifica que el idioma es español.

Sección head:

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currículum de Tío Gilito</title>
    <style>
        /* Estilos CSS aquí */
    </style>
</head>

Contiene metadatos, el título de la página y estilos CSS internos.

Metaetiquetas:

    <meta charset="UTF-8">: Define la codificación de caracteres.

    <meta name="viewport" ...>: Optimiza la visualización en dispositivos móviles.

Título de la página:

<title>Currículum de Tío Gilito</title>

Estilos CSS internos:

<style>
    /* Estilos CSS aquí */
</style>

Define los estilos para varios elementos HTML, incluyendo el body, contenedor principal, encabezados, tablas y la imagen de perfil.

Cuerpo del documento:

<body>
    <div class="container">
        <!-- Contenido aquí -->
    </div>
</body>



Contiene el contenido visible de la página, envuelto en un div con clase "container".

Esta estructura proporciona un marco básico para un currículum vitae en formato web, con estilos predefinidos para mejorar la presentación y la legibilidad.

Estilo del cuerpo (body):

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 20px;
    background-color: #f4f4f4;
}
Define la fuente, el espaciado entre líneas, los márgenes, el relleno y el 
color de fondo para todo el cuerpo del documento.


Estilo del contenedor principal:
.container {
    max-width: 800px;
    margin: auto;
    background: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}
Define un contenedor con un ancho máximo, centrado, con fondo blanco, bordes 
redondeados y una sombra sutil.


Estilo de los encabezados:
h1, h2 {
    color: #333;
}
Define el color de los encabezados h1 y h2.


Estilo de las tablas:
table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
}
th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}
th {
    background-color: #f2f2f2;
}
Define el aspecto de las tablas, incluyendo bordes, relleno y color de fondo
para los encabezados.


Estilo de la imagen de perfil:
.profile-img {
    float: right;
    margin-left: 20px;
    border-radius: 50%;
}
Define el estilo para la imagen de perfil, haciéndola flotar a la derecha y 
dándole una forma circular.

Estas reglas CSS se definen dentro de la etiqueta <style> en el <head> del 
documento HTML. Cada regla comienza con un selector (como body, .container, 
h1, h2, etc.) seguido de un bloque de declaraciones entre llaves {}. Cada 
declaración consiste en una propiedad y un valor, separados por dos puntos : 
y terminando con un punto y coma ;.

# EJERCICIO 03

