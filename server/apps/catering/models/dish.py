from django.db import models

from apps.catering.models.establishments import Establishment
from apps.catering.models.ingredient import Ingredient

class Dish(models.Model):
    """Модель блюда."""
    name = models.CharField(
        max_length=100,
        help_text='Название блюда')
    photo = models.ImageField(
        upload_to='dish_photos',
        help_text='Фото блюда',
        blank=True,)
    total_callories = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        default=0,
        help_text='Суммарное количество калорий в блюде',
        )
    cost = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        default=0,
        help_text='Стоимость блюда',
        )
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='ingredients',
        help_text='id ингредиентов, входящих в состав блюда',
        )
    place = models.ForeignKey(
        Establishment,
        on_delete=models.CASCADE,
        help_text='Заведение, в котором подают данное блюдо',
        )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
