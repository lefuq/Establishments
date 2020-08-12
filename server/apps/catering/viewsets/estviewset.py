from rest_framework.viewsets import ModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.main.permissions.permissions import IsOwnerOrReadOnly

from apps.catering.models.establishments import Establishment
from apps.catering.serializers.estserializer import EstSerializer

class EstViewSet(ModelViewSet):
    """Viewset для заведений.
    Создание заведений доступно только авторизованным пользователям.
    Редактирование заведения доступно только владельцу заведения.
    Подключена фильтрация для url-запросов и запросов через api.
    Просмотр заведений доступен всем.

    """
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = EstSerializer
    queryset = Establishment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
