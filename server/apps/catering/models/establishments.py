from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Establishment(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField()
    work_time = models.CharField(max_length=10, help_text='Введите время работы заведения в формате "С XX до YY"')
    address = models.CharField(max_length=150)
    coordinates = models.CharField(max_length=30, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    avg_cost = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name
