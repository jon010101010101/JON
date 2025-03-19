class Text(str):
    """
    Clase para manejar texto con escape automático de caracteres HTML
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
    Clase base para elementos HTML
    """
    class ValidationError(Exception):
        pass

    def __init__(self, tag='div', content=None, attr=None, tag_type='double'):
        self.tag = tag
        self.attr = attr or {}
        self.content = []
        self.tag_type = tag_type
        
        if content:
            self.add_content(content)

    def __str__(self):
        attrs = ''.join(f' {k}="{v}"' for k, v in sorted(self.attr.items()))
        result = f"<{self.tag}{attrs}>"
        
        if self.tag_type == 'double':
            content = self._format_content()
            result += f"{content}</{self.tag}>"
        return result

    def _format_content(self):
        if not self.content:
            return ""
        return '\n' + '\n'.join(
            f"  {line}" 
            for item in self.content 
            for line in str(item).split('\n')
        ) + '\n'

    def add_content(self, content):
        if not self._check_content_type(content):
            raise self.ValidationError()
            
        if isinstance(content, list):
            self.content += [c for c in content if c != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def _check_content_type(content):
        return isinstance(content, (Elem, Text)) or \
              (isinstance(content, list) and all(isinstance(c, (Elem, Text)) for c in content))

