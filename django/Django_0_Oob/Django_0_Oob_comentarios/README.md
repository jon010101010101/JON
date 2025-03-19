# EJERCICIO 00

. template es una plantilla que sirve como base para crear documentos o páginas web. Sus principales características son:

Contiene elementos predefinidos de diseño y estructura que se pueden personalizar.

Se utiliza comúnmente en desarrollo web y sistemas de gestión de contenidos como WordPress.

Puede incluir código HTML, CSS y otros lenguajes de programación web.

Permite mantener una apariencia consistente en múltiples páginas o documentos.

Facilita la creación rápida de contenido al proporcionar una estructura base.

En WordPress, los archivos .template son parte de un tema y controlan cómo se muestra el contenido en diferentes secciones del sitio.

Pueden ser archivos de texto que contienen marcadores de posición para ser reemplazados con contenido específico.








# ELERCICIO 05



# Definición de la clase Text que hereda de str
class Text(str):
    """
    Clase Text para manejar texto con escape automático de caracteres HTML.
    Hereda de str.
    """

    # Método para convertir el objeto Text a string
    def __str__(self):
        """
        Devuelve la representación en cadena del objeto Text.
        Escapa caracteres especiales de HTML y convierte saltos de línea en etiquetas <br />.
        """
        # Llama al método __str__ de la clase padre (str) y aplica reemplazos
        return super().__str__().replace('&', '&amp;')\
            .replace('<', '&lt;')\
            .replace('>', '&gt;')\
            .replace('"', '&quot;')\
            .replace('\n', '\n<br />\n')

# Definición de la clase Elem para representar elementos HTML
class Elem:
    """
    Clase base para representar elementos HTML.
    """

    # Definición de una excepción personalizada para errores de validación
    class ValidationError(Exception):
        """
        Excepción personalizada para errores de validación en la clase Elem.
        """
        pass  # No se requiere implementación adicional

    # Método constructor de la clase Elem
    def __init__(self, tag='div', content=None, attr=None, tag_type='double'):
        """
        Inicializa un objeto Elem.

        :param tag: Nombre de la etiqueta HTML (por defecto 'div').
        :param content: Contenido del elemento (puede ser Text, Elem o una lista de estos).
        :param attr: Diccionario de atributos HTML (por defecto vacío).
        :param tag_type: Tipo de etiqueta ('double' para etiquetas con cierre, 'simple' para auto-cerradas).
        """
        self.tag = tag  # Asigna el nombre de la etiqueta
        self.attr = attr or {}  # Asigna los atributos o un diccionario vacío si no se proporcionan
        self.content = []  # Inicializa el contenido como una lista vacía
        self.tag_type = tag_type  # Asigna el tipo de etiqueta

        # Si se proporciona contenido, lo añade al elemento
        if content:
            self.add_content(content)

    # Método para convertir el objeto Elem a string (representación HTML)
    def __str__(self):
        """
        Devuelve la representación en cadena del objeto Elem como HTML.
        """
        # Genera la cadena de atributos HTML
        attrs = ''.join(f' {k}="{v}"' for k, v in sorted(self.attr.items()))
        # Crea la etiqueta de apertura con sus atributos
        result = f"<{self.tag}{attrs}>"

        # Si es una etiqueta doble, añade el contenido y la etiqueta de cierre
        if self.tag_type == 'double':
            content = self._format_content()  # Formatea el contenido
            result += f"{content}</{self.tag}>"
        
        return result  # Devuelve la representación HTML completa

    # Método privado para formatear el contenido del elemento
    def _format_content(self):
        """
        Formatea el contenido del elemento con la indentación adecuada.
        """
        # Si no hay contenido, devuelve una cadena vacía
        if not self.content:
            return ""
        
        # Formatea el contenido con indentación
        return '\n' + '\n'.join(
            f"  {line}"  # Añade dos espacios de indentación a cada línea
            for item in self.content  # Itera sobre cada elemento del contenido
            for line in str(item).split('\n')  # Divide el contenido en líneas
        ) + '\n'

    # Método para añadir contenido al elemento
    def add_content(self, content):
        """
        Añade contenido al elemento.

        :param content: Contenido a añadir (Text, Elem o una lista de estos).
        :raises ValidationError: Si el tipo de contenido no es válido.
        """
        # Verifica si el tipo de contenido es válido
        if not Elem._check_content_type(content):
            raise Elem.ValidationError()  # Lanza una excepción si no es válido

        # Si el contenido es una lista, añade cada elemento que no sea un Text vacío
        if isinstance(content, list):
            self.content += [c for c in content if c != Text('')]
        # Si no es un Text vacío, lo añade directamente
        elif content != Text(''):
            self.content.append(content)

    # Método estático para verificar el tipo de contenido
    @staticmethod
    def _check_content_type(content):
        """
        Comprueba si el contenido es de un tipo válido (Text, Elem o una lista de estos).

        :param content: Contenido a comprobar.
        :return: True si es válido, False en caso contrario.
        """
        # Verifica si el contenido es una instancia de Elem o Text, o una lista de estos
        return (isinstance(content, (Elem, Text)) or
                (isinstance(content, list) and all(isinstance(c, (Elem, Text)) for c in content)))
