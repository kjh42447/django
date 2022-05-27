from atexit import register
import imp
from django import template

register = template.Library()

@register.filter        #템플릿 필터를 함수로 사용가능하도록 함
def sub(value, arg):
    return value - arg