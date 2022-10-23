from django import template
from .ExplicitFilter.main import ExplicitFilter

register = template.Library()


@register.filter()
def censor(string):
    result = ExplicitFilter(string)
    return result.changing()
