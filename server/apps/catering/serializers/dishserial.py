from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.catering.models.dish import Dish
from apps.catering.models.establishments import Establishment

class DishSerializer(ModelSerializer):

    class Meta:
        model = Dish
        fields = '__all__'

    def create(self, validated_data):
        dish = Dish.objects.create(
            name = validated_data['name'],
            photo = validated_data['photo'],
            cost = validated_data['cost'],
            place = validated_data['place'])
        dish.ingredients.set(validated_data['ingredients'])
        return dish
