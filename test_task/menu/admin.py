from django.contrib import admin
from .models import Menu, FirstLevel, SecondLevel, ThirdLevel

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Параметры отображения модели Menu."""

    list_display = (
        'name',
        'slug',
    )
    search_fields = ('name', )
    list_filter = ('name', )
    empty_value_display = '-пусто-'


@admin.register(FirstLevel)
class FirstLevelAdmin(admin.ModelAdmin):
    """Параметры отображения модели FirstLevel."""

    list_display = (
        'name',
        'slug',
        'menu',
    )
    search_fields = ('name', )
    list_filter = ('name', )
    empty_value_display = '-пусто-'


@admin.register(SecondLevel)
class SecondLevelAdmin(admin.ModelAdmin):
    """Параметры отображения модели SecondLevel."""

    list_display = (
        'name',
        'slug',
        'first_level',
    )
    search_fields = ('name', )
    list_filter = ('name', )
    empty_value_display = '-пусто-'


@admin.register(ThirdLevel)
class ThirdLevelAdmin(admin.ModelAdmin):
    """Параметры отображения модели ThirdLevel."""

    list_display = (
        'name',
        'slug',
        'second_level',
    )
    search_fields = ('name', )
    list_filter = ('name', )
    empty_value_display = '-пусто-'
