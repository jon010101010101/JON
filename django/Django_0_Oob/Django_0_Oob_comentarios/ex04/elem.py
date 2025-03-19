class Text(str):
    """
    Una clase Text para representar texto que podrías usar con tus elementos HTML.

    Porque usar directamente la clase str era demasiado convencional.
    """

    def __str__(self):
        """
        Devuelve la representación en cadena del objeto Text.
        
        Este método sustituye los caracteres especiales de HTML y convierte los saltos de
         línea en etiquetas <br />. Para que se puedan mostrar en HTML.
        """
        return super().__str__().replace('&', '&amp;')\
            .replace('<', '&lt;')\
            .replace('>', '&gt;')\
            .replace('"', '&quot;')\
            .replace('\n', '\n<br />\n')


class Elem:
    """
    Elem nos permitirá representar nuestros elementos HTML.
    """

    class ValidationError(Exception):
        """
        Excepción personalizada para errores de validación en la clase Elem.
        """
        def __init__(self):
            super().__init__("Error: comportamiento incorrecto.")

    def __init__(self, tag='div', attr=None, content=None, tag_type='double'):
        """
        Inicializa un objeto Elem.

        :param tag: Nombre de la etiqueta HTML
        :param attr: Diccionario de atributos HTML
        :param content: Contenido del elemento (puede ser Text, Elem, o una lista de estos)
        :param tag_type: 'double' para elementos con etiquetas de cierre, 'simple' para 
        etiquetas auto-cerradas
        """
        self.tag = tag  # Define el nombre de la etiqueta HTML
        self.attr = attr if attr is not None else {}  # Define los atributos del elemento
        self.content = []  # Inicializa el contenido como una lista vacía
        self.tag_type = tag_type  # Define el tipo de etiqueta ('double' o 'simple')

        if content is not None:
            self.add_content(content)  # Añade el contenido inicial si existe

    def __str__(self):
        """
        Devuelve la representación en cadena del objeto Elem como HTML.
        """
        attributes = self.__make_attr()  # Genera la representación en cadena de los atributos
        result = f"<{self.tag}{attributes}>"  # Comienza la representación del elemento con su etiqueta y atributos
        
        if self.tag_type == 'double':  # Si es una etiqueta doble, añade contenido y etiqueta de cierre
            content = self.__make_content()
            result += f"{content}</{self.tag}>"
        
        return result

    def __make_attr(self):
        """
        Genera la representación en cadena de los atributos del elemento.
        """
        return ''.join(f' {k}="{v}"' for k, v in sorted(self.attr.items()))  # Convierte los atributos al formato HTML

    def __make_content(self):
        """
        Genera la representación en cadena del contenido del elemento.
        
        Indenta correctamente cada línea del contenido.
        """
        if not self.content:  # Si no hay contenido, devuelve una cadena vacía
            return ""
        
        content_str = ""
        
        for elem in self.content:  # Itera sobre cada elemento en el contenido
            elem_str = str(elem)  # Convierte el elemento a cadena
            if elem_str:
                # Aplica sangría a cada línea del contenido para mantener la estructura HTML correcta
                indented = "\n".join(f"  {line}" for line in elem_str.split('\n'))
                content_str += f"\n{indented}"
        
        return f"{content_str}\n" if content_str else ""  # Devuelve el resultado con un salto al final si no está vacío

    def add_content(self, content):
        """
        Añade contenido al elemento.

        :param content: Contenido a añadir (Text, Elem, o una lista de estos)
        :raises ValidationError: Si el tipo de contenido no es válido
        """
        if not Elem.check_type(content):  # Comprueba si el tipo de contenido es válido
            raise Elem.ValidationError()
        
        if isinstance(content, list):  # Si el contenido es una lista, añade cada elemento que no sea un Text vacío
            self.content.extend([elem for elem in content if elem != Text('')])
        
        elif content != Text(''):  # Si el contenido no es un Text vacío, lo añade directamente
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Comprueba si el contenido es de un tipo válido (Text, Elem, o una lista de estos).

        :param content: Contenido a comprobar
        :return: True si es válido, False en caso contrario
        """
        return (isinstance(content, Elem) or
                isinstance(content, Text) or
                (isinstance(content, list) and all(isinstance(c, (Elem, Text)) for c in content)))


if __name__ == '__main__':
    pass