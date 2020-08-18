from rest_framework.viewsets import ModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.main.permissions.permissions import IsOwnerOrReadOnly

from apps.catering.models.establishments import Establishment
from apps.catering.serializers.estserializer import EstSerializer

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

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

    @method_decorator(cache_page(60*15))
    def dispatch(self, *args, **kwargs):
        return super(EstViewSet, self).dispatch(*args, **kwargs)
