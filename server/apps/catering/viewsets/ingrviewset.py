from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.catering.models.ingredient import Ingredient
from apps.catering.serializers.ingrserial import IngrSerializer

class IngrViewSet(GenericViewSet, ListModelMixin):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = IngrSerializer
    queryset = Ingredient.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
