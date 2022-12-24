from django import template
from django.shortcuts import get_object_or_404

from ..models import Menu

register = template.Library()

@register.inclusion_tag('menu/menu_detail.html')
def draw_menu(slug, url):
    url_list = url.strip('/').split('/')
    url_last = url_list[-1]
    url_first = url_list[1]
    menu = get_object_or_404(Menu, slug=slug)
    return {'menu': menu, 'url': url_last, 'url_first': url_first}
