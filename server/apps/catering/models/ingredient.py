from django.db import models

class Ingredient(models.Model):
    """Модель ингредиента."""
    name = models.CharField(
        max_length=100,
        blank=True,
        help_text='Название ингредиента',
        )
    callories = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0,
        help_text='Энергетическая ценность (килокалории)',
        )

    def __str__(self):
        return self.name
