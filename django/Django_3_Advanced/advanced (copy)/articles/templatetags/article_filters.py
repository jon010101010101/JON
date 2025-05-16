from django import template
from django.utils.timesince import timesince
from django.utils import timezone
from django.utils.translation import get_language

register = template.Library()

@register.filter
def my_truncate_synopsis(value):
    """
    Trunca la sinopsis a 20 caracteres exactos (incluyendo los puntos suspensivos).
    Si el texto es más largo, muestra los primeros 17 caracteres y añade '...'.
    """
    if not isinstance(value, str):
        value = str(value)
    if len(value) > 20:
        return value[:17] + '...'
    return value

@register.filter
def ago(value):
    """
    Devuelve el tiempo transcurrido desde 'value' hasta ahora, adaptando el prefijo/sufijo
    según el idioma activo.
    """
    if not value:
        return ''
    lang = get_language()
    now = timezone.now()
    delta = timesince(value, now)
    if lang and lang.startswith('es'):
        return f"hace {delta}"
    elif lang and lang.startswith('fr'):
        return f"il y a {delta}"
    else:
        return f"{delta} ago"
