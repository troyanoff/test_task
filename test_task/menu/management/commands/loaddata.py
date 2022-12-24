from django.core.management.base import BaseCommand

from ...models import Menu, FirstLevel, SecondLevel, ThirdLevel

fl = FirstLevel.objects.all()
class Command(BaseCommand):
    help = 'Загружает объекты и таблиц csv в БД.'

    def handle(self, *args, **kwargs):
        menu = Menu.objects.all()
        d = 1
        for m in menu:
            for i in range(3):
                FirstLevel.objects.create(
                    name=f'Первый уровень №{i+1}',
                    slug=f'fl{i+1}m{d}',
                    menu=m
                )
            d += 1
        fl = FirstLevel.objects.all()
        d = 1
        for first in fl:
            for i in range(3):
                SecondLevel.objects.create(
                    name=f'Второй уровень №{i+1}',
                    slug=f'sl{i+1}fl{d}',
                    first_level=first
                )
            d += 1

        sl = SecondLevel.objects.all()
        d = 1
        for second in sl:
            for i in range(3):
                ThirdLevel.objects.create(
                    name=f'Третий уровень №{i+1}',
                    slug=f'tl{i+1}sl{d}',
                    second_level=second
                )
            d += 1
        
        self.stdout.write('Объекты загруженны в базу данных.')
