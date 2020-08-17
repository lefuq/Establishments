from django.db import models
from django.contrib.auth.models import User

class Establishment(models.Model):
    """Модель заведения."""
    name = models.CharField(
        max_length=100,
        help_text='Название заведения',)
    photo = models.ImageField(
        upload_to='place_photos',
        help_text='Фотография заведения',)
    work_time = models.CharField(
        max_length=10,
        blank=True,
        help_text='Время работы заведения в формате "С XX до YY"')
    address = models.CharField(
        max_length=150,
        blank=True,
        help_text='Адрес заведения',)
    coordinates = models.CharField(
        max_length=30,
        blank=True,
        help_text='Координаты заведения (широта/долгота)',)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text='Пользователь, зарегистрировавший заведение')
    avg_cost = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        default=0,
        help_text='Средняя стоимость блюд в заведении',
        )

    def __str__(self):
        return self.name
