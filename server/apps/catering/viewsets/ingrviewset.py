from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from apps.catering.models.ingredient import Ingredient
from apps.catering.serializers.ingrserial import IngrSerializer

class IngrViewSet(GenericViewSet, ListModelMixin):
    serializer_class = IngrSerializer
    queryset = Ingredient.objects.all()
