from rest_framework.viewsets import ModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend

from apps.catering.models.dish import Dish
from apps.catering.serializers.dishserial import DishSerializer

class DishViewSet(ModelViewSet):
    serializer_class = DishSerializer
    queryset = Dish.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'    
