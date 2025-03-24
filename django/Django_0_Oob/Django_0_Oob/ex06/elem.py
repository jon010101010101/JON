class Text(str):
    """
    A class for handling text with automatic HTML character escaping.
    """
    def __str__(self):
        return super().__str__()\
            .replace('&', '&amp;')\
            .replace('<', '&lt;')\
            .replace('>', '&gt;')\
            .replace('"', '&quot;')\
            .replace('\n', '\n<br />\n')


class Elem:
    """
    Base class for HTML elements.
    """
    class ValidationError(Exception):
        pass

    def __init__(self, tag='div', content=None, attr=None, tag_type='double'):
        """
        Initialize an HTML element.

        :param tag: HTML tag name
        :param content: Element content (can be Text, Elem, or a list of these)
        :param attr: Dictionary of HTML attributes
        :param tag_type: 'double' for elements with closing tags, 'simple' for self-closing tags
        """
        self.tag = tag
        self.attr = attr or {}
        self.content = []
        self.tag_type = tag_type
        
        if content:
            self.add_content(content)

    def __str__(self):
        """
        Return the string representation of the HTML element.
        """
        attrs = ''.join(f' {k}="{v}"' for k, v in sorted(self.attr.items()))
        result = f"<{self.tag}{attrs}>"
        
        if self.tag_type == 'double':
            content = self._format_content()
            result += f"{content}</{self.tag}>"
        return result

    def _format_content(self):
        """
        Format the content of the element with proper indentation.
        """
        if not self.content:
            return ""
        return '\n' + '\n'.join(
            f"  {line}" 
            for item in self.content 
            for line in str(item).split('\n')
        ) + '\n'

    def add_content(self, content):
        """
        Add content to the element.

        :param content: Content to add (Text, Elem, or a list of these)
        :raises ValidationError: If content type is invalid
        """
        if not self._check_content_type(content):
            raise self.ValidationError()
            
        if isinstance(content, list):
            # Add non-empty content from the list
            self.content += [c for c in content if c != Text('')]
        elif content != Text(''):
            # Add single non-empty content
            self.content.append(content)

    @staticmethod
    def _check_content_type(content):
        """
        Check if the content is of a valid type (Text, Elem, or a list of these).

        :param content: Content to check
        :return: True if valid, False otherwise
        """
        return isinstance(content, (Elem, Text)) or \
              (isinstance(content, list) and all(isinstance(c, (Elem, Text)) for c in content))
