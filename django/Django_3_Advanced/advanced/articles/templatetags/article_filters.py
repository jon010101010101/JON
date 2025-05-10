from django import template
from django.utils.timesince import timesince
from django.utils import timezone
from django.utils.translation import get_language

register = template.Library()

@register.filter
def truncate_synopsis(value, max_length=20):
    """
    Truncates the synopsis to max_length characters (including '...').
    If the text is longer, shows the first max_length - 3 and adds '...'.
    """
    if not isinstance(value, str):
        value = str(value)
    if len(value) > max_length:
        return value[:max_length - 3] + '...'
    return value

@register.filter
def ago(value):
    """
    Returns the time since 'value' until now, with the correct suffix/prefix
    depending on the active language:
    - English: '1 week, 2 days ago'
    - Spanish: 'hace 1 semana, 2 días'
    - French:  'il y a 1 semaine, 2 jours'
    """
    if not value:
        return ''
    lang = get_language()
    delta = timesince(value, timezone.now())
    if lang.startswith('es'):
        return f"hace {delta}"
    elif lang.startswith('fr'):
        return f"il y a {delta}"
    else:
        return f"{delta} ago"
