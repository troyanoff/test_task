from models import FirstLevel, SecondLevel, ThirdLevel

fl = FirstLevel.objects.all()

for first in fl:
    d = 1
    for i in range(3):
        SecondLevel.objects.create(
            name=f'Второй уровень №{i+1}',
            slug=f'sl{i+1}fl{d}',
            first_level=first
        )
        d += 1

sl = SecondLevel.objects.all()

for first in fl:
    d = 1
    for i in range(3):
        SecondLevel.objects.create(
            name=f'Второй уровень №{i+1}',
            slug=f'sl{i+1}fl{d}',
            first_level=first
        )
        d += 1