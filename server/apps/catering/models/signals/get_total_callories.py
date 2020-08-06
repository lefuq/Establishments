from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.db.models import Sum

from apps.catering.models.dish import Dish
from apps.catering.models.ingredient import Ingredient

@receiver(m2m_changed, sender=Dish.ingredients.through)
def generate_total_callories(sender, instance, **kwargs):
    instance.total_callories = (Dish.objects.get(pk=instance.id)
                .ingredients.values_list('callories')
                .aggregate(Sum('callories'))['callories__sum'])
    return instance.save
