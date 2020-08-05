from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100, blank=True)
    callories = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.name
