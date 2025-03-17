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





# EJERCICIO 03

**Para ejecutar**
google-chrome cv.html

**Estructura básica**
<html>: Es la etiqueta raíz que envuelve todo el contenido de la página.
<head>: Contiene metadatos y enlaces a recursos externos.
<body>: Encierra todo el contenido visible de la página web.

**Encabezados**
<h1> a <h6>: Definen encabezados de diferentes niveles, donde <h1> es el más importante y <h6> el menos importante.

**Párrafos y texto**
<p>: Define un párrafo de texto.

<strong>: Se usa para poner texto en negrita.

**Enlaces**
<a href="URL">: Crea un enlace a otra página o recurso.

**Tablas**
<table>: Define una tabla.
<th>: Representa una celda de encabezado en una tabla.
<tr>: Define una fila en una tabla.
<td>: Representa una celda de datos en una tabla.

**Listas**
<ul>: Crea una lista no ordenada.
<ol>: Crea una lista ordenada.
<li>: Define cada elemento de una lista.

**Elementos semánticos**
<header>: Define la sección introductoria de la página.
<nav>: Especifica los elementos de navegación.
<main>: Contiene el contenido principal del documento.

Cada etiqueta tiene una apertura <etiqueta> y un cierre </etiqueta>, excepto algunas como <img> que son de cierre automático.


# Paso 1: Estructura Básica

<!DOCTYPE html> 
<!-- Declara que este es un documento HTML5. Es obligatorio para que los navegadores interpreten correctamente el código. -->
<html lang="es"> 
<!-- Define el idioma principal del contenido como español (lang="es"). Esto es útil para navegadores y motores de búsqueda. -->

<head>
    <!-- Metadatos y estilos van aquí -->
    <meta charset="UTF-8"> 
    <!-- Define el conjunto de caracteres como UTF-8, lo que permite usar caracteres especiales como tildes y eñes -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
    <!-- Configura la ventana gráfica para que la página sea responsive, adaptándose a diferentes tamaños de pantalla -->
    <title>Currículum Vitae</title> 
    <!-- Define el título de la página que aparecerá en la pestaña del navegador -->
    <style>
        /* Estilos para el cuerpo y contenedor */
        body {
            font-family: Arial, sans-serif; /* Define la fuente principal como Arial, con una alternativa sans-serif */
            line-height: 1.6; /* Ajusta el espaciado entre líneas para mejorar la legibilidad */
            margin: 0; /* Elimina los márgenes predeterminados del body */
            padding: 20px; /* Añade un espacio interno alrededor del contenido del body */
            background-color: #f4f4f4; /* Establece un color de fondo gris claro para toda la página */
        }
        .container {
            max-width: 800px; /* Limita el ancho máximo del contenedor a 800 píxeles */
            margin: auto; /* Centra el contenedor horizontalmente en la página */
            background: #fff; /* Establece un fondo blanco para el contenedor */
            padding: 20px; /* Añade un espacio interno de 20 píxeles dentro del contenedor */
            border-radius: 5px; /* Redondea las esquinas del contenedor con un radio de 5 píxeles */
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* Aplica una sombra sutil alrededor del contenedor */
        }
        h1, h2 {
            color: #333; /* Establece el color del texto de los encabezados como gris oscuro (#333) */
        }
        /* Estilos para la tabla */
        table {
            width: 100%; /* La tabla ocupa el 100% del ancho del contenedor */
            border-collapse: collapse; /* Fusiona los bordes de las celdas adyacentes (bordes colapsados) */
        }
        table, th, td {
            border: 1px solid black; /* Aplica bordes sólidos y negros a la tabla, encabezados y celdas */
        }
        th {
            background-color: #f2f2f2; /* Establece un fondo gris claro (#f2f2f2) para las celdas de encabezado (th) */
        }
    </style>
</head>

<body>
    <!-- Todo el contenido visible va dentro del cuerpo (body) -->
    <div class="container">
        <!-- Contenedor principal que agrupa todo el contenido -->
        <!-- Paso 4: Encabezado principal -->
        <h1>Jon Urrutia Araolaza</h1>
        <p style="font-weight: bold;"></p>
        <!-- Paso 5: Información Personal -->
        <h2>Información Personal</h2>
        <p>
            Correo: jurrutia@student42.com<br>
            Teléfono: +34 (255) 255-255<br>
            Ubicación: Getxo
        </p>
        <!-- Paso 6: Habilidades -->
        <h2>Habilidades</h2>
        <ul>
            <li>Gestión de Personal</li>
            <li>Prevención de Riesgos</li>
            <li>Programación Python, Machine Learning e IA</li>
            <li>Gestión Financiera</li>
        </ul>
        <!-- Paso 7: Trayectoria Profesional -->
        <h2>Trayectoria Profesional</h2>
        <ol>
            <li>CEO y Propietario de Construcciones Jon (2004 - Presente)</li>
        </ol>
        <!-- Paso 8: Logros Financieros -->
        <h2>Logros Financieros</h2>
        <table>
            <tr>
                <th>Año</th>
                <th>Logro</th>
                <th>Impacto</th>
            </tr>
            <tr>
                <td>2004</td>
                <td>Fundación de Construcciones Jon</td>
                <td>Empresa más importante del sector</td>
            </tr>
            <tr>
                <td>2010</td>
                <td>Construcción de la Torre Iberdrola</td>
                <td>Edificio más alto de Bilbao</td>
            </tr>
            <!-- Celda inferior derecha con borde especial -->
            <tr>
                <td>2023</td>
                <td>Expansión internacional</td>
                <td style="border-right-color: #424242; border-bottom-color: #424242;">Expansión por 15 países</td>
            </tr>
        </table>
        <!-- Paso 9: Educación -->
        <h2>Educación</h2>
        <!-- Párrafos estilizados con bordes azules -->
        <p style="border: 1px solid blue; padding: 10px;">Amago de programador en Python, Machine Learning e IA</p>
        <p style="border: 1px solid blue; padding: 10px;">Estudiante Urduliz 42</p>
    </div><!-- Fin del contenedor principal -->
</body>

</html>

# EJERCICIO 02

**Para ejecutar**
google-chrome form.html

<!-- Declaración del tipo de documento HTML5 -->
<!DOCTYPE html>

<!-- Elemento raíz del documento HTML, especificando el idioma como español -->
<html lang="es">
<head>
    <!-- Codificación de caracteres UTF-8 para soportar caracteres internacionales -->
    <meta charset="UTF-8">
    <!-- Configuración para dispositivos móviles, estableciendo el ancho de la vista al ancho del dispositivo y escalado inicial -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Título de la página que aparece en la barra de título del navegador -->
    <title>Formulario de Contacto</title>
    <!-- Enlace a un archivo JavaScript externo llamado popup.js -->
    <script src="popup.js"></script>
    <!-- Bloque de estilos CSS para el formulario -->
    <style>
        /* Reducir el espacio entre los elementos del formulario */
        form label, form input, form button {
            /* Espacio reducido entre elementos */
            margin-bottom: 5px; 
        }
        /* Espaciado reducido para el grupo de género */
        form div {
            margin-bottom: 5px; 
        }
    </style>
</head>

<!-- Cuerpo del documento HTML, donde se muestra el contenido visible -->
<body>
    <!-- Formulario con un ID "contactForm" -->
    <form id="contactForm">
        <!-- Campo para el nombre -->
        <label for="firstname">Nombre:</label>
        <!-- Entrada de texto para el nombre, obligatoria y con un ancho visible de 31 caracteres -->
        <input type="text" id="firstname" name="firstname" required size="31"><br>
        <!-- Campo para el apellido -->
        <label for="name">Apellido:</label>
        <!-- Entrada de texto para el apellido, obligatoria y con un ancho visible de 30 caracteres -->
        <input type="text" id="name" name="name" required size="30"><br>
        <!-- Campo para la edad -->
        <label for="age">Edad:</label>
        <!-- Entrada numérica para la edad, obligatoria y con un ancho visible de 203 caracteres -->
        <input type="number" id="age" name="age" required size="203"><br>
        <!-- Campo para el teléfono -->
        <label for="phone">Teléfono:</label>
        <!-- Entrada de teléfono, obligatoria y con un ancho visible de 30 caracteres -->
        <input type="tel" id="phone" name="phone" required size="30"><br>
        <!-- Campo para el correo electrónico -->
        <label for="email">Correo electrónico:</label>
        <!-- Entrada de correo electrónico, obligatoria y con un ancho visible de 22 caracteres -->
        <input type="email" id="email" name="email" required size="22"><br>
        <!-- Campo para preguntar si es estudiante de 42 años -->
        <label for="student">¿Estudiante de 42 años?:</label>
        <!-- Casilla de verificación para la pregunta -->
        <input type="checkbox" id="student" name="student"><br>
        <!-- Campo para el género -->
        <!-- Contenedor para las opciones de género, mostradas en línea -->
        <div style="display: inline-block;">
            <!-- Opción de radio para género masculino -->
            <input type="radio" id="gender_male" name="gender" value="Masculino">
            <label for="gender_male">Masculino</label>
            <!-- Opción de radio para género femenino -->
            <input type="radio" id="gender_female" name="gender" value="Femenino">
            <label for="gender_female">Femenino</label>
            <!-- Opción de radio para otro género -->
            <input type="radio" id="gender_other" name="gender" value="Otro">
            <label for="gender_other">Otro</label>
        </div><br>
        <!-- Botón de envío -->
        <!-- Botón genérico con un ancho de 200 píxeles y estilo azul. 
            El boton cuando se pulsa se pone gris onmousedown y cuando se envia vuelve a ser 
            onmouseup azul-->
        <button type="button" 
                onclick="displayFormContents()" 
                style="width: 200px; background-color: #007BFF; color: white; border: none; padding: 10px; cursor: pointer;" 
                onmousedown="this.style.background='gray'" 
                onmouseup="this.style.background='#007BFF'">Enviar</button>
    </form>
</body>
</html>


# EJERCICIO 03

**Para ejecutar**
google-chrome copy.html
NOTA: No sale exactamente como el subjct perro es por que han modificado el java scricpt, aunque cambie colores esta correcto

<!DOCTYPE html> <!-- Declaración del tipo de documento HTML5 -->
<html lang="en"> <!-- Elemento raíz del documento HTML, especificando el idioma como inglés -->
<head> <!-- Sección de metadatos y recursos del documento -->
  <meta charset="UTF-8"> <!-- Especifica la codificación de caracteres del documento -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- Configura la vista para dispositivos móviles -->
  <title>Replicating Web Page</title> <!-- Título de la página que aparece en la pestaña del navegador -->
  <link rel="stylesheet" href="style.css"> <!-- Enlaza el archivo CSS externo para los estilos -->
</head>
<body> <!-- Cuerpo del documento, contiene el contenido visible -->
    <!-- Lista de habilidades de desarrollo web -->
    <ul> <!-- Lista no ordenada para agrupar las secciones de habilidades -->
        <li> <!-- Elemento de lista para las habilidades de Frontend -->
            <h2>Frontend</h2> <!-- Encabezado para la sección de Frontend -->
            <!-- Habilidad HTML5 -->
            <p class="html5" style="width: 80%" data-value="80">HTML5</p> <!-- Párrafo para mostrar el nombre de la habilidad y su porcentaje -->
            <progress class="html5" value="80" max="100"></progress> <!-- Barra de progreso para representar visualmente el nivel de habilidad -->
            <!-- Habilidad CSS3 -->
            <p class="css3" style="width: 60%" data-value="60">CSS3</p>
            <progress class="css3" value="60" max="100"></progress>
            <!-- Habilidad jQuery -->
            <p class="jquery" style="width: 50%" data-value="50">jQuery</p>
            <progress class="jquery" value="50" max="100"></progress>
        </li>
        <!-- Elemento de lista para las habilidades de Backend -->
        <li>
            <h2>Backend</h2> <!-- Encabezado para la sección de Backend -->
            <!-- Habilidad Python -->
            <p class="python" style="width: 75%" data-value="75">Python</p>
            <progress class="python" value="75" max="100"></progress>
            <!-- Habilidad PHP -->
            <p class="php" style="width: 65%" data-value="65">PHP</p>
            <progress class="php" value="65" max="100"></progress>
            <!-- Habilidad Node.js -->
            <p class="node-js" style="width: 35%" data-value="35">Node.js</p>
            <progress class="node-js" value="35" max="100"></progress>
        </li>
    </ul>
</body>
</html>


# EJERCICIO 04

En la terminal se pone python3 -m http.server 8000, si no entra 8001, 8002etc

Se abre el navegador y se pone http://localhost:8000

Y sale esto:

Listado de directorios para /
archivo1.js
archivo2.js
archivo3.js
archivo4.js
snippets.html

haciendo click en snippets.html

ejecuta y sale un mensaje de localhost:8000 says
Exercice réussi!


Explicación del flujo de ejecución
Orden de carga: Los archivos se cargan en este orden: file4.js, file1.js, file3.js, file2.js.

Definición de funciones:

file4.js define puffin()

file1.js define unicorn()

file3.js define whale()

file2.js define cat()

Cadena de llamadas:

file2.js llama a cat()

cat() llama a whale()

whale() llama a unicorn()

unicorn() llama a puffin()

puffin() muestra la alerta "Exercice réussi!"


# EJERCICIO 05

Hay que comprobar que es correcto o los fallos que da en:
https://validator.w3.org

copia codigo y pegar en validar por entrada directa y dar a controlar

Si esta bien sale y sino salen los errores que tiene
Verificación de documentos completada. No se muestran errores ni advertencias.


**Línea 1** : Añade <!DOCTYPE html> al principio del documento.

Línea 1: Elimina el atributo type y cierra correctamente la etiqueta script:
    
<script src="jquery-1.12.2.min.js"></script>
Línea 2-4: Mueve la etiqueta <head> antes del <script> y corrige el charset:
    
<head> <meta charset="UTF-8"> </head>

**Línea 6**: Elimina la barra diagonal al final:
    
<link rel="stylesheet" href="style.css">

**Línea 32**: Corrige la etiqueta de cierre h1 a h2 y añade un valor al href:
    
<h2 class="article-title"><a href="#">Opening Date Announced</a></h2>

**Línea 40**: Elimina la etiqueta <p> dentro de <b>:
<b class="article-lead">The Art Gallery will be opening to an <em>invitation-only</em> group of art enthusiasts across the country on <strong>December 1, 2013</strong>.</b>
    
**Línea 52**: Cierra correctamente la etiqueta p:
    
</p>

**Línea 59**: Cambia <strong> por <em>:
    
<p class="article-date"><em>Published on</em>:
Línea 85: Corrige la etiqueta de cierre times a time:
<time datetime="2013-09-12">September 12, 2013</time>
    
**Línea 90**: Elimina un &:
    
<p><a href="#">Read More &raquo;</a></p>

**Línea 104**: Añade un valor al href:
<a href="#">Read More »</a>
    
**Línea 115**: Corrige la etiqueta de cierre asside a aside:
    
</aside>
**Línea 124**: Cierra correctamente la etiqueta a:
    
<li><a href="#">About</a></li>
