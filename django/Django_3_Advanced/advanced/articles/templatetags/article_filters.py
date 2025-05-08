from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def truncate_synopsis(value, max_length=20):
    """
    Trunca la sinopsis a max_length caracteres y añade '...' si es más larga.
    """
    if not isinstance(value, str):
        value = str(value)
    if len(value) > max_length:
        return value[:max_length] + '...'
    return value

@register.filter
def ago(value):
    """
    Devuelve una cadena como '2 days ago' usando timesince.
    """
    from django.utils.timesince import timesince
    if value:
        return timesince(value, timezone.now()) + ' ago'
    return ''
