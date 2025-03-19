from elem import Elem, Text

class Html(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='html', content=content, attr=attr)

class Head(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='head', content=content, attr=attr)

class Body(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='body', content=content, attr=attr)

class Title(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='title', content=content, attr=attr)

class Meta(Elem):
    def __init__(self, attr=None):
        super().__init__(tag='meta', tag_type='simple', attr=attr)

class Img(Elem):
    def __init__(self, attr=None):
        super().__init__(tag='img', tag_type='simple', attr=attr)

class Table(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='table', content=content, attr=attr)

class Th(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='th', content=content, attr=attr)

class Tr(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='tr', content=content, attr=attr)

class Td(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='td', content=content, attr=attr)

class Ul(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='ul', content=content, attr=attr)

class Ol(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='ol', content=content, attr=attr)

class Li(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='li', content=content, attr=attr)

class H1(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='h1', content=content, attr=attr)

class H2(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='h2', content=content, attr=attr)

class P(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='p', content=content, attr=attr)

class Div(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='div', content=content, attr=attr)

class Span(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='span', content=content, attr=attr)

class Hr(Elem):
    def __init__(self, attr=None):
        super().__init__(tag='hr', tag_type='simple', attr=attr)

class Br(Elem):
    def __init__(self, attr=None):
        super().__init__(tag='br', tag_type='simple', attr=attr)

if __name__ == "__main__":
    # Demostración de elementos simples
    print("Elementos simples:")
    print(Br())
    print(Hr())
    print()

    # Demostración de elementos con contenido
    print("Elementos con contenido:")
    print(H1(Text("Título")))
    print(P(Text("Párrafo")))
    print()

    # Demostración de elementos anidados
    print("Elementos anidados:")
    doc = Html([
        Head(Title(Text("Título de la Página"))),
        Body([
            H1(Text("Encabezado Principal")),
            P(Text("Un párrafo"))
        ])
    ])
    print(doc)
    print()

    # Demostración de elementos con atributos
    print("Elementos con atributos:")
    img = Img(attr={"src": "imagen.jpg", "alt": "Una imagen"})
    print(img)
    print()

    # Demostración de elementos de lista
    print("Elementos de lista:")
    ul = Ul([
        Li(Text("Elemento 1")),
        Li(Text("Elemento 2")),
        Li(Text("Elemento 3"))
    ])
    print(ul)
