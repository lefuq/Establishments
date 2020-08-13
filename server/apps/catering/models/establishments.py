from django.db import models
from django.contrib.auth.models import User

class Establishment(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='place_photos')
    work_time = models.CharField(
        max_length=10,
        blank=True,
        help_text='Введите время работы заведения в формате "С XX до YY"')
    address = models.CharField(max_length=150, blank=True)
    coordinates = models.CharField(max_length=30, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    avg_cost = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        default=0,
        )

    def __str__(self):
        return self.name
