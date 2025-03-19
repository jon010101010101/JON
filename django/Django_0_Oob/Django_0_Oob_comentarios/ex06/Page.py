# Importamos la clase base Elem desde elem.py
from elem import Elem

# Importamos todas las clases específicas de HTML desde elements.py
from elements import Html, Head, Body, Title, H1, P, Ul, Ol, Li, Div, H2, Table, Tr, Th, Td, Span, Text

# Definimos la clase Page para manejar páginas HTML completas
class Page:
    """
    Clase Page para representar y validar páginas HTML completas.
    """

    def __init__(self, elem):
        """
        Constructor de la clase Page.

        :param elem: Un objeto que hereda de Elem y representa la raíz del árbol HTML.
        :raises TypeError: Si elem no es una instancia de Elem.
        """
        if not isinstance(elem, Elem):  # Verifica que elem sea una instancia de Elem
            raise TypeError("Page debe inicializarse con una instancia de Elem")
        self.elem = elem  # Asigna el elemento raíz a un atributo interno

    def is_valid(self):
        """
        Valida si la estructura del árbol HTML cumple con las reglas especificadas.

        :return: True si el árbol es válido; False en caso contrario.
        """
        return self._validate_tree(self.elem)  # Llama al método privado para validar el árbol

    def _validate_tree(self, elem):
        """
        Método privado que valida recursivamente la estructura del árbol HTML.

        :param elem: El nodo actual del árbol a validar.
        :return: True si el nodo y su subárbol son válidos; False en caso contrario.
        """
        # Lista de etiquetas HTML válidas
        valid_types = {'html', 'head', 'body', 'title', 'meta', 'img', 'table', 'th', 'tr', 'td',
                       'ul', 'ol', 'li', 'h1', 'h2', 'p', 'div', 'span', 'hr', 'br'}

        if isinstance(elem, Text):  # Si es un nodo de texto (Text), siempre es válido
            return True

        if not isinstance(elem, Elem) or elem.tag not in valid_types:  # Verifica que sea un Elem válido
            return False

        # Validación específica para la etiqueta <html>
        if elem.tag == 'html':
            if len(elem.content) != 2 or not isinstance(elem.content[0], Head) or not isinstance(elem.content[1], Body):
                return False

        # Validación específica para la etiqueta <head>
        elif elem.tag == 'head':
            if len([e for e in elem.content if isinstance(e, Title)]) != 1:  # Debe contener exactamente un <title>
                return False

        # Validación específica para las etiquetas <body> y <div>
        elif elem.tag in ['body', 'div']:
            for child in elem.content:
                if not isinstance(child, (H1, H2, Div, Table, Ul, Ol, Span, P)):  # Solo ciertos elementos son válidos
                    return False

        # Validación específica para etiquetas que solo pueden contener un texto
        elif elem.tag in ['title', 'h1', 'h2', 'li', 'th', 'td']:
            if len(elem.content) != 1 or not isinstance(elem.content[0], Text):  # Debe contener exactamente un Text
                return False

        # Validación específica para la etiqueta <p>
        elif elem.tag == 'p':
            if not all(isinstance(child, Text) for child in elem.content):  # Solo puede contener nodos de texto
                return False

        # Validación específica para la etiqueta <span>
        elif elem.tag == 'span':
            if not all(isinstance(child, (Text, P)) for child in elem.content):  # Puede contener texto o párrafos (<p>)
                return False

        # Validación específica para las etiquetas <ul> y <ol>
        elif elem.tag in ['ul', 'ol']:
            if len(elem.content) < 1 or not all(isinstance(child, Li) for child in elem.content):  # Deben contener al menos un <li>
                return False

        # Validación específica para la etiqueta <tr>
        elif elem.tag == 'tr':
            if len(elem.content) < 1:  # Debe contener al menos un hijo
                return False
            if not all(isinstance(child, Th) for child in elem.content) and not all(isinstance(child, Td) for child in elem.content):
                return False  # No puede mezclar <th> y <td> en la misma fila

        # Validación específica para la etiqueta <table>
        elif elem.tag == 'table':
            if not all(isinstance(child, Tr) for child in elem.content):  # Solo puede contener filas (<tr>)
                return False

        # Valida recursivamente los hijos del nodo actual
        return all(self._validate_tree(child) for child in elem.content)

    def __str__(self):
        """
        Devuelve una representación en cadena de la página HTML.

        :return: La representación HTML completa como cadena.
                 Incluye el DOCTYPE si el elemento raíz es <html>.
        """
        if isinstance(self.elem, Html):  # Si el elemento raíz es Html
            return "<!DOCTYPE html>\n<meta charset=\"UTF-8\">\n" + str(self.elem)
        return str(self.elem)

    def write_to_file(self, filename):
        """
        Escribe el código HTML en un archivo.

        :param filename: Nombre del archivo donde se escribirá el HTML.
                         El archivo incluirá el DOCTYPE si el elemento raíz es Html.
                         La codificación será UTF-8.
        """
        with open(filename, 'w', encoding='utf-8') as f:  # Abre el archivo en modo escritura con codificación UTF-8
            f.write(str(self))  # Escribe la representación HTML en el archivo

if __name__ == "__main__":
    # Prueba 1: Página HTML válida
    html_valido = Html([
        Head(Title(Text("Página de prueba"))),
        Body([
            H1(Text("Bienvenido")),
            P(Text("Este es un párrafo de ejemplo.")),
            Ul([
                Li(Text("Elemento 1")),
                Li(Text("Elemento 2"))
            ]),
            Div([
                H2(Text("Subtítulo")),
                Table([
                    Tr([Th(Text("Encabezado 1")), Th(Text("Encabezado 2"))]),
                    Tr([Td(Text("Dato 1")), Td(Text("Dato 2"))])
                ])
            ])
        ])
    ])
    pagina_valida = Page(html_valido)
    print("Prueba 1 - Página válida:")
    print("Es válida:", pagina_valida.is_valid())
    print(pagina_valida)
    pagina_valida.write_to_file("pagina_valida.html")
    print()

    # Prueba 2: Página HTML inválida (sin Head)
    html_invalido = Html([
        Body([H1(Text("Título sin Head"))])
    ])
    pagina_invalida = Page(html_invalido)
    print("Prueba 2 - Página inválida (sin Head):")
    print("Es válida:", pagina_invalida.is_valid())
    print()

    # Prueba 3: Página con estructura inválida en Body
    html_invalido_body = Html([
        Head(Title(Text("Página inválida"))),
        Body([
            H1(Text("Título")),
            Text("Texto suelto en Body")  # Esto no está permitido directamente en Body
        ])
    ])
    pagina_invalida_body = Page(html_invalido_body)
    print("Prueba 3 - Página con estructura inválida en Body:")
    print("Es válida:", pagina_invalida_body.is_valid())
    print()

    # Prueba 4: Página con lista vacía (inválida)
    html_lista_vacia = Html([
        Head(Title(Text("Lista vacía"))),
        Body([
            Ul([])  # Lista vacía, debe contener al menos un Li
        ])
    ])
    pagina_lista_vacia = Page(html_lista_vacia)
    print("Prueba 4 - Página con lista vacía:")
    print("Es válida:", pagina_lista_vacia.is_valid())
    print()

    # Prueba 5: Página con tabla inválida
    html_tabla_invalida = Html([
        Head(Title(Text("Tabla inválida"))),
        Body([
            Table([
                Tr([Th(Text("Encabezado")), Td(Text("Dato"))])  # Mezcla Th y Td en la misma fila
            ])
        ])
    ])
    pagina_tabla_invalida = Page(html_tabla_invalida)
    print("Prueba 5 - Página con tabla inválida:")
    print("Es válida:", pagina_tabla_invalida.is_valid())
    print()

    # Prueba 6: Página con span conteniendo elementos no permitidos
    html_span_invalido = Html([
        Head(Title(Text("Span inválido"))),
        Body([
            Span([
                Text("Texto válido"),
                Div(Text("Div no permitido en Span"))  # Div no está permitido dentro de Span
            ])
        ])
    ])
    pagina_span_invalido = Page(html_span_invalido)
    print("Prueba 6 - Página con span inválido:")
    print("Es válida:", pagina_span_invalido.is_valid())
