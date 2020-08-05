from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.catering.models.dish import Dish
from apps.catering.models.ingredient import Ingredient


@receiver(post_save, sender=Dish)
def generate_total_callories(sender, instance, **kwargs):
    if not instance.total_callories:
        instance.total_callories = float(sum([Ingredient.objects.get(id=i).callories for i in instance.ingredients]))
        instance.save()
