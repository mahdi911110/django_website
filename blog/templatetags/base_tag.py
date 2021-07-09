from django import template
from .. import models

register = template.Library()

@register.simple_tag
def title(data = 'bootstrap'):
    return data

@register.inclusion_tag("blog/partials/category_navbar.html")
def category_navbar():
    category = models.Category.objects.active()
    cat = {'category':category}
    return cat