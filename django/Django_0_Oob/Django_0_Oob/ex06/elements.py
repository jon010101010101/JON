from elem import Elem, Text

class Html(Elem):
    """
    Represents the <html> element.
    """
    def __init__(self, content=None, attr=None):
        super().__init__(tag='html', content=content, attr=attr)

class Head(Elem):
    """
    Represents the <head> element.
    """
    def __init__(self, content=None, attr=None):
        super().__init__(tag='head', content=content, attr=attr)

class Body(Elem):
    """
    Represents the <body> element.
    """
    def __init__(self, content=None, attr=None):
        super().__init__(tag='body', content=content, attr=attr)

class Title(Elem):
    """
    Represents the <title> element.
    """
    def __init__(self, content=None, attr=None):
        super().__init__(tag='title', content=content, attr=attr)

class Meta(Elem):
    """
    Represents the <meta> element (self-closing).
    """
    def __init__(self, attr=None):
        super().__init__(tag='meta', tag_type='simple', attr=attr)

class Img(Elem):
    """
    Represents the <img> element (self-closing).
    """
    def __init__(self, attr=None):
        super().__init__(tag='img', tag_type='simple', attr=attr)

class Table(Elem):
    """
    Represents the <table> element.
    """
    def __init__(self, content=None, attr=None):
        super().__init__(tag='table', content=content, attr=attr)

class Th(Elem):
    """
    Represents the <th> element (table header cell).
    """
    def __init__(self, content=None, attr=None):
        super().__init__(tag='th', content=content, attr=attr)

class Tr(Elem):
    """
    Represents the <tr> element (table row).
    """
    def __init__(self, content=None, attr=None):
        super().__init__(tag='tr', content=content, attr=attr)

class Td(Elem):
    """
    Represents the <td> element (table cell).
    """
    def __init__(self, content=None, attr=None):
        super().__init__(tag='td', content=content, attr=attr)

class Ul(Elem):
    """
    Represents the <ul> element (unordered list).
    """
    def __init__(self, content=None, attr=None):
        super().__init__(tag='ul', content=content, attr=attr)

class Ol(Elem):
    """
    Represents the <ol> element (ordered list).
    """
    def __init__(self, content=None, attr=None):
        super().__init__(tag='ol', content=content, attr=attr)

class Li(Elem):
    """
    Represents the <li> element (list item).
    """
    def __init__(self, content=None, attr=None):
        super().__init__(tag='li', content=content, attr=attr)

class H1(Elem):
    """
    Represents the <h1> element (header level 1).
    """
    def __init__(self, content=None, attr=None):
        super().__init__(tag='h1', content=content, attr=attr)

class H2(Elem):
    """
    Represents the <h2> element (header level 2).
    """
    def __init__(self, content=None, attr=None):
        super().__init__(tag='h2', content=content, attr=attr)

class P(Elem):
    """
    Represents the <p> element (paragraph).
    """
    def __init__(self, content=None, attr=None):
        super().__init__(tag='p', content=content, attr=attr)

class Div(Elem):
    """
    Represents the <div> element.
    """
    def __init__(self, content=None, attr=None):
        super().__init__(tag='div', content=content, attr=attr)

class Span(Elem):
    """
    Represents the <span> element.
    """
    def __init__(self, content=None, attr=None):
        super().__init__(tag='span', content=content, attr=attr)

class Hr(Elem):
    """
    Represents the <hr> element (horizontal rule - self-closing).
    """
    def __init__(self, attr=None):
        super().__init__(tag='hr', tag_type='simple', attr=attr)

class Br(Elem):
    """
    Represents the <br> element (line break - self-closing).
    """
    def __init__(self, attr=None):
        super().__init__(tag='br', tag_type='simple', attr=attr)


if __name__ == "__main__":
    
	# Demonstration of simple elements
	print("Simple elements:")
	print(Br())  # Line break
	print(Hr())  # Horizontal rule
	print()

	# Demonstration of elements with text-based content
	print("Elements with text-based content:")
	print(H1(Text("Title")))  # Header level 1 with text
	print(P(Text("Paragraph")))  # Paragraph with text
	print()

	# Demonstration of nested elements
	print("Nested elements:")
	doc = Html([
		Head(Title(Text("Page Title"))),  # Title inside head
		Body([
			H1(Text("Main Header")),  # Header inside body
			P(Text("A paragraph"))  # Paragraph inside body
		])
	])
	print(doc)
	print()

	# Demonstration of elements with attributes
	print("Elements with attributes:")
	img = Img(attr={"src": "image.jpg", "alt": "An image"})  # Image with attributes
	print(img)
	print()

	# Demonstration of list elements
	print("List elements:")
	ul = Ul([
		Li(Text("Item 1")),  # List item 1
		Li(Text("Item 2")),  # List item 2
		Li(Text("Item 3"))   # List item 3
	])
	print(ul)
