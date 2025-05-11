from django import template
from django.utils import timezone
from django.utils.translation import gettext as _

register = template.Library()

@register.filter
def truncate_synopsis(s, length=20):
    if not s:
        return ''
    return s if len(s) <= length else s[:length-3] + '...'

@register.filter
def ago(dt):
    if not dt:
        return ''
    delta = timezone.now() - dt
    weeks = delta.days // 7
    days = delta.days % 7
    parts = []
    if weeks:
        parts.append(_("%(count)d week%(plural)s") % {'count': weeks, 'plural': 's' if weeks != 1 else ''})
    if days:
        parts.append(_("%(count)d day%(plural)s") % {'count': days, 'plural': 's' if days != 1 else ''})
    if not parts:
        return _("today")
    return ", ".join(parts) + _(" ago")
