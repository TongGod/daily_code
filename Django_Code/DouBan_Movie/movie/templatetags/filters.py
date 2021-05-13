from django import template

register = template.Library()  # 注册


@register.filter(name="get_url")
def get_url(value):
    return str(value)[:22]
