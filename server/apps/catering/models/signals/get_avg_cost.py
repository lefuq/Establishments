from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.db.models import Avg

from apps.catering.models.dish import Dish
from apps.catering.models.establishments import Establishment

@receiver(m2m_changed, sender=Dish.place.through)
def generate_avg_cost(sender, instance, **kwargs):
    instance.avg_cost = Dish.objects.filter(place=instance.id).aggregate(Avg('cost'))['cost__avg']
    return instance.save()
