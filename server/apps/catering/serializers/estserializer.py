from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.catering.models.establishments import Establishment

from django.contrib.auth.models import User
from yandex_geocoder import Client
from apps.catering.secrets import yandex_api_key

client = Client(yandex_api_key)

class EstSerializer(ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),
    default=serializers.CurrentUserDefault())

    class Meta:
        model = Establishment
        fields = '__all__'
        read_only_fields = ('coordinates', 'avg_cost')

    def create(self, validated_data):
        try:
            coord = client.coordinates(validated_data['address'])
        except:
            return 'Введен некорректный адрес'
        return Establishment.objects.create(
            coordinates=', '.join([str(i) for i in coord]),
            **validated_data)
