from rest_framework.viewsets import ModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.main.permissions.permissions import IsEstOwnerOrReadOnly

from apps.catering.models.dish import Dish
from apps.catering.serializers.dishserial import DishSerializer

class DishViewSet(ModelViewSet):
    """Viewset для блюд.
    Создание и редактирование блюд доступно только владельцам заведений.
    Подключена фильтрация для url-запросов и запросов через api.
    Просмот блюд доступен всем.

    """
    permission_classes = [IsAuthenticatedOrReadOnly, IsEstOwnerOrReadOnly]
    serializer_class = DishSerializer
    queryset = Dish.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
