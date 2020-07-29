from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.catering.models.establishments import Establishment

from django.contrib.auth.models import User
from yandex_geocoder import Client
from apps.catering.secrets import yandex_api_key

client = Client(yandex_api_key)

class EstSerializer(ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())
    id = serializers.HiddenField(default=Establishment.objects.latest('id').id+1)

    class Meta:
        model = Establishment
        fields = '__all__'
        read_only_fields = ('coordinates', 'avg_cost')

    def create(self, validated_data):
        establishment = Establishment.objects.create(**validated_data)
        coord = client.coordinates(establishment.address)
        establishment.coordinates = ', '.join([str(i) for i in coord])
        establishment.save()
        return establishment
