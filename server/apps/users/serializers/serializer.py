from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(ModelSerializer):
    token = serializers.SerializerMethodField('get_token')

    class Meta:
        model = User
        fields = ('username', 'password', 'token')
        extra_kwargs = ({'password': {'write_only': True}})

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.save()
        return user

    def get_token(self, object):
        return Token.objects.create(user=User.objects.latest('id')).key
