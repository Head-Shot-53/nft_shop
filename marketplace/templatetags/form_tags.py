from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, css_value):
    return value.as_widget(attrs = {'class':css_value})