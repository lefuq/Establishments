from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from url_filter.integrations.drf import DjangoFilterBackend

from apps.catering.models.ingredient import Ingredient
from apps.catering.serializers.ingrserial import IngrSerializer

class IngrViewSet(GenericViewSet, ListModelMixin):
    serializer_class = IngrSerializer
    queryset = Ingredient.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
