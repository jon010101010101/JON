from elem import Elem
from elements import Html, Head, Body, Title, H1, P, Ul, Ol, Li, Div, H2, Table, Tr, Th, Td, Span, Text

class Page:
    """
    Class to represent and validate complete HTML pages.
    """

    def __init__(self, elem):
        """
        Initializes a Page object.

        :param elem: An object inheriting from Elem representing the root of the HTML tree.
        :raises TypeError: If elem is not an instance of Elem.
        """
        if not isinstance(elem, Elem):  # Check if elem is an instance of Elem
            raise TypeError("Page must be initialized with an instance of Elem")
        self.elem = elem  # Assign the root element to an internal attribute

    def is_valid(self):
        """
        Validates if the HTML tree structure complies with the specified rules.

        :return: True if the tree is valid; False otherwise.
        """
        return self._validate_tree(self.elem)  # Call the private method to validate the tree

    def _validate_tree(self, elem):
        """
        Private method that recursively validates the HTML tree structure.

        :param elem: The current node of the tree to validate.
        :return: True if the node and its subtree are valid; False otherwise.
        """
        # List of valid HTML tags
        valid_types = {'html', 'head', 'body', 'title', 'meta', 'img', 'table', 'th', 'tr', 'td',
                       'ul', 'ol', 'li', 'h1', 'h2', 'p', 'div', 'span', 'hr', 'br'}

        if isinstance(elem, Text):  # If it's a text node (Text), it's always valid
            return True

        if not isinstance(elem, Elem) or elem.tag not in valid_types:  # Check if it's a valid Elem
            return False

        # Specific validation for the <html> tag
        if elem.tag == 'html':
            if len(elem.content) != 2 or not isinstance(elem.content[0], Head) or not isinstance(elem.content[1], Body):
                return False

        # Specific validation for the <head> tag
        elif elem.tag == 'head':
            if len([e for e in elem.content if isinstance(e, Title)]) != 1:  # Must contain exactly one <title>
                return False

        # Specific validation for the <body> and <div> tags
        elif elem.tag in ['body', 'div']:
            for child in elem.content:
                if not isinstance(child, (H1, H2, Div, Table, Ul, Ol, Span, P, Text)):  # Only certain elements are valid
                    return False

        # Specific validation for tags that can only contain text
        elif elem.tag in ['title', 'h1', 'h2', 'li', 'th', 'td']:
            if len(elem.content) != 1 or not isinstance(elem.content[0], Text):  # Must contain exactly one Text
                return False

        # Specific validation for the <p> tag
        elif elem.tag == 'p':
            if not all(isinstance(child, Text) for child in elem.content):  # Can only contain text nodes
                return False

        # Specific validation for the <span> tag
        elif elem.tag == 'span':
            if not all(isinstance(child, (Text, P)) for child in elem.content):  # Can contain text or paragraphs (<p>)
                return False

        # Specific validation for the <ul> and <ol> tags
        elif elem.tag in ['ul', 'ol']:
            if len(elem.content) < 1 or not all(isinstance(child, Li) for child in elem.content):  # Must contain at least one <li>
                return False

        # Specific validation for the <tr> tag
        elif elem.tag == 'tr':
            if len(elem.content) < 1:  # Must contain at least one child
                return False
            th_count = sum(isinstance(child, Th) for child in elem.content)
            td_count = sum(isinstance(child, Td) for child in elem.content)
            if th_count > 0 and td_count > 0:
                return False  # Cannot mix <th> and <td> in the same row
            if th_count == 0 and td_count == 0:
                return False #must have at least one th or td

        # Specific validation for the <table> tag
        elif elem.tag == 'table':
            if not all(isinstance(child, Tr) for child in elem.content):  # Can only contain rows (<tr>)
                return False

        # Recursively validate the children of the current node
        return all(self._validate_tree(child) for child in elem.content)

    def __str__(self):
        """
        Returns a string representation of the HTML page.

        :return: The complete HTML representation as a string.
                 Includes the DOCTYPE if the root element is <html>.
        """
        if isinstance(self.elem, Html):  # If the root element is Html
            return "<!DOCTYPE html>\n<meta charset=\"UTF-8\">\n" + str(self.elem)
        return str(self.elem)

    def write_to_file(self, filename):
        """
        Writes the HTML code to a file.

        :param filename: Name of the file where the HTML will be written.
                         The file will include the DOCTYPE if the root element is Html.
                         The encoding will be UTF-8.
        """
        with open(filename, 'w', encoding='utf-8') as f:  # Open the file in write mode with UTF-8 encoding
            f.write(str(self))  # Write the HTML representation to the file

if __name__ == "__main__":
    # Test 1: Valid HTML Page
    valid_html = Html([
        Head(Title(Text("Test Page"))),
        Body([
            H1(Text("Welcome")),
            P(Text("This is a sample paragraph.")),
            Ul([
                Li(Text("Item 1")),
                Li(Text("Item 2"))
            ]),
            Div([
                H2(Text("Subtitle")),
                Table([
                    Tr([Th(Text("Header 1")), Th(Text("Header 2"))]),
                    Tr([Td(Text("Data 1")), Td(Text("Data 2"))])
                ])
            ])
        ])
    ])
    valid_page = Page(valid_html)
    print("Test 1 - Valid Page:")
    print("Is valid:", valid_page.is_valid())
    print(valid_page)
    valid_page.write_to_file("valid_page.html")
    print()

    # Test 2: Invalid HTML Page (missing Head)
    invalid_html = Html([
        Body([H1(Text("Title without Head"))])
    ])
    invalid_page = Page(invalid_html)
    print("Test 2 - Invalid Page (missing Head):")
    print("Is valid:", invalid_page.is_valid())
    print()

    # Test 3: Invalid HTML Page (invalid structure in Body)
    invalid_html_body = Html([
        Head(Title(Text("Invalid Page"))),
        Body([
            H1(Text("Title")),
            Text("Loose text in Body")  # This is not allowed directly in Body
        ])
    ])
    invalid_page_body = Page(invalid_html_body)
    print("Test 3 - Invalid Page (invalid structure in Body):")
    print("Is valid:", invalid_page_body.is_valid())
    print()

    # Test 4: Page with empty list (invalid)
    html_empty_list = Html([
        Head(Title(Text("Empty List"))),
        Body([
            Ul([])  # Empty list, must contain at least one Li
        ])
    ])
    pagina_lista_vacia = Page(html_empty_list)
    print("Test 4 - Page with empty list:")
    print("Is valid:", pagina_lista_vacia.is_valid())
    print()

    # Test 5: Page with invalid table
    html_invalid_table = Html([
        Head(Title(Text("Invalid Table"))),
        Body([
            Table([
                Tr([Th(Text("Header")), Td(Text("Data"))])  # Mix Th and Td in the same row
            ])
        ])
    ])
    pagina_tabla_invalida = Page(html_invalid_table)
    print("Test 5 - Page with invalid table:")
    print("Es válida:", pagina_tabla_invalida.is_valid())
    print()

    # Test 6: Page with span containing not allowed elements
    html_span_invalido = Html([
        Head(Title(Text("Invalid Span"))),
        Body([
            Span([
                Text("Valid Text"),
                Div(Text("Div not allowed in Span"))  # Div not allowed inside Span
            ])
        ])
    ])
    pagina_span_invalido = Page(html_span_invalido)
    print("Test 6 - Page with invalid span:")
    print("Is valid:", pagina_span_invalido.is_valid())
