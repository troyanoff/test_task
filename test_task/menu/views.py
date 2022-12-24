from django.shortcuts import get_object_or_404,render

from .models import Menu, FirstLevel, SecondLevel, ThirdLevel


def index(request):
    """Настройка отображения главной страницы."""
    menus = Menu.objects.all()
    context = {
        'menus': menus,
    }
    template = 'menu/index.html'

    return render(request, template, context)

def menu(request, menu_slug):
    menu = get_object_or_404(
        Menu.objects.select_related(),
        slug=menu_slug
    )

    context = {
        'menu': menu,
    }
    template = 'menu/menu.html'

    return render(request, template, context)

def first(request, menu_slug, fl_slug):
    menu = get_object_or_404(
        Menu.objects.select_related(),
        slug=menu_slug
    )
    first = menu.first_level.get(
        slug=fl_slug
    )

    context = {
        'menu': menu,
        'first': first,
    }
    template = 'menu/menu.html'

    return render(request, template, context)

def second(request, menu_slug, fl_slug, sl_slug):
    menu = get_object_or_404(
        Menu.objects.select_related(),
        slug=menu_slug
    )
    second = menu.first_level.get(slug=fl_slug).second_level.get(
        slug=sl_slug
    )


    context = {
        'menu': menu,
        'second': second,
    }
    template = 'menu/menu.html'

    return render(request, template, context)

def third(request, menu_slug, fl_slug, sl_slug, tl_slug):
    menu = get_object_or_404(
        Menu.objects.select_related(),
        slug=menu_slug
    )
    third = menu.first_level.get(slug=fl_slug).second_level.get(
        slug=sl_slug
    ).third_level.get(slug=tl_slug)


    context = {
        'menu': menu,
        'third': third,
    }
    template = 'menu/menu.html'

    return render(request, template, context)
