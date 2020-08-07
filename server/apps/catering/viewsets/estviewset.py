from rest_framework.viewsets import ModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend

from apps.catering.models.establishments import Establishment
from apps.catering.serializers.estserializer import EstSerializer

class EstViewSet(ModelViewSet):
    serializer_class = EstSerializer
    queryset = Establishment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
