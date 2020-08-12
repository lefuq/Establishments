from django.db import models

from apps.catering.models.establishments import Establishment
from apps.catering.models.ingredient import Ingredient

class Dish(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='dish_photos')
    total_callories = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        default=0,
        )
    cost = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        default=0,
        )
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='ingredients'
        )
    place = models.ForeignKey(
        Establishment,
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return self.name
