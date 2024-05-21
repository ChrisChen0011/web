from django import template

register = template.Library()

@register.filter(name='capitalize_first_letter')
def capitalize_first_letter(value):
    if value:
        return value.capitalize()
    return value
