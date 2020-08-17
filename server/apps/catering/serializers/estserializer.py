from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.catering.models.establishments import Establishment
from apps.catering.models.dish import Dish

from django.contrib.auth.models import User
from yandex_geocoder import Client
from apps.catering.secrets import yandex_api_key

client = Client(yandex_api_key)
"""Ключ авторизации в api для дальнейшего получения координат заведения."""

class EstSerializer(ModelSerializer):
    """Сериалайзер заведения.
    При создании заведения автоматически присваивается владелец (залогиненый
    пользователь). Собирается список блюд в скрытое поле для фильтрации за-
    ведений по блюду.

    """
    owner = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault(),
        )
    dishes = serializers.HiddenField(
        default = serializers.SerializerMethodField('get_dishes'),
        )

    class Meta:
        model = Establishment
        fields = '__all__'
        read_only_fields = ('coordinates', 'avg_cost', 'dishes')

    def create(self, validated_data):
        """Метод создания блюда.
        При создании собираются данные об адресе и через api Яндекса конверти-
        руются в координаты в формате широта/долгота.

        """
        try:
            coord = client.coordinates(validated_data['address'])
        except:
            return 'Введен некорректный адрес'
        validated_data.pop('dishes')
        return Establishment.objects.create(
            coordinates=', '.join([str(i) for i in coord]),
            **validated_data
            )

    def get_dishes(self, request):
        """Получение списка блюд, привязанных к заведению."""
        dishes = Dish.objects.filter(place = request.id).values_list('id')
        dishes_list = [i[0] for i in dishes]
        return dishes_list
