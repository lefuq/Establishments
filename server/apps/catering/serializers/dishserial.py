from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.catering.models.dish import Dish
from rest_framework.fields import CurrentUserDefault
from rest_framework.exceptions import NotAuthenticated

class DishSerializer(ModelSerializer):
    """Сериалайзер блюда."""
    class Meta:
        model = Dish
        fields = '__all__'

    def create(self, validated_data):
        """Создание блюда. При создании блюда собираются данные
        о калориях ингредиентов и считается общая калорийность блюда.
        
        """
        ingredients = validated_data.pop('ingredients')
        dish = Dish.objects.create(**validated_data)
        dish.ingredients.set(ingredients)
        for i in ingredients:
            dish.total_callories += i.callories
        dish.save()
        return dish
