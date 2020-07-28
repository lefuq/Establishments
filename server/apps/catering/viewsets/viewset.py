from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import CreateModelMixin

from apps.catering.models.establishments import Establishment
from apps.catering.serializers.serializer import EstSerializer

class EstViewSet(ModelViewSet):
    serializer_class = EstSerializer
    queryset = Establishment.objects.all()
