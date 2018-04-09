from django import template
import time

register = template.Library()

@register.filter(name='counter')
def counter(list, index):
    return list[index]


