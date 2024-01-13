from django import template
from shop.models import *


register = template.Library()

@register.simple_tag()
def get_products(filter=None):
    if not filter:
        return Product.objects.all()
    else:
        return Product.objects.filter(pk=filter)