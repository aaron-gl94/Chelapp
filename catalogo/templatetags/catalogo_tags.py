from django import template
register = template.Library()
from django.db.models import Count
from ..models import Category, Product

@register.simple_tag
def FilterCategory():
    return Category.objects.all()

@register.inclusion_tag('catalogo/related.html')
def show_related(category=None, count=3):
    related = Product.objects.all().filter(category=category)[:count]
    return {
        'related':related,
    }
