from rest_framework.viewsets import ModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.catering.models.dish import Dish
from apps.catering.serializers.dishserial import DishSerializer

class DishViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = DishSerializer
    queryset = Dish.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
