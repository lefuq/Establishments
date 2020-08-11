from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.catering.models.dish import Dish
from rest_framework.fields import CurrentUserDefault
from rest_framework.exceptions import NotAuthenticated

class DishSerializer(ModelSerializer):

    class Meta:
        model = Dish
        fields = '__all__'

    def create(self, validated_data):
        ingredients = validated_data.pop('ingredients')
        dish = Dish.objects.create(**validated_data)
        dish.ingredients.set(ingredients)
        for i in ingredients:
            dish.total_callories += i.callories
        dish.save()
        return dish
