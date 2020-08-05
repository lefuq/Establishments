from django.db import models
from django.contrib.postgres.fields import ArrayField
from apps.catering.models.establishments import Establishment

class Dish(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='dish_photos')
    total_callories = models.DecimalField(max_digits=8, decimal_places=2, blank=True, default=0)
    cost = models.DecimalField(max_digits=8, decimal_places=2, blank=True, default=0)
    ingredients = ArrayField(models.PositiveIntegerField(blank=True))
    place = models.ManyToManyField(Establishment, related_name='places')

    def __str__(self):
        return self.name
