from django.db import models

class Menu(models.Model):
    """Модель меню."""
    name = models.CharField(
        verbose_name='Название',
        max_length=100,
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Уникальное обозначение',
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        """Вывод названия меню."""
        return self.name


class FirstLevel(models.Model):
    """Список первого уровня."""
    name = models.CharField(
        verbose_name='Название',
        max_length=100,
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Уникальное обозначение',
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='first_level',
        verbose_name='Меню',
    )

    class Meta:
        verbose_name = 'Первый уровень'
        verbose_name_plural = 'Первые уровни'

    def __str__(self):
        """Вывод названия."""
        return self.name


class SecondLevel(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=100,
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Уникальное обозначение',
    )
    first_level = models.ForeignKey(
        FirstLevel,
        on_delete=models.CASCADE,
        related_name='second_level',
        verbose_name='Первый уровень',
    )

    class Meta:
        verbose_name = 'Второй уровень'
        verbose_name_plural = 'Вторые уровни'

    def __str__(self):
        """Вывод названия."""
        return self.name

class ThirdLevel(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=100,
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Уникальное обозначение',
    )
    second_level = models.ForeignKey(
        SecondLevel,
        on_delete=models.CASCADE,
        related_name='third_level',
        verbose_name='Первый уровень',
    )

    class Meta:
        verbose_name = 'Третий уровень'
        verbose_name_plural = 'Третьи уровни'

    def __str__(self):
        """Вывод названия."""
        return self.name
