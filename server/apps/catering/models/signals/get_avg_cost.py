from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg

from apps.catering.models.dish import Dish
from apps.catering.models.establishments import Establishment

@receiver(post_save, sender=Dish)
def generate_avg_cost(sender, instance, created, **kwargs):
    if created:
        est = instance.place
        est.avg_cost = (Dish.objects.filter(place=est.id)
                .aggregate(Avg('cost'))['cost__avg'])
        return est.save()
