from rest_framework.serializers import ModelSerializer

from apps.test.models import Test


class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'name', 'random_string')
        extra_kwargs = {'random_string':{'read_only': True}}
