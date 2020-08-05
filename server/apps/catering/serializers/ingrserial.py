from rest_framework.serializers import ModelSerializer
from apps.catering.models.ingredient import Ingredient

class IngrSerializer(ModelSerializer):

    class Meta:
        model = Ingredient
        fields = '__all__'
