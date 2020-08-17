from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(ModelSerializer):
    """Сериалайзер пользователя.
    При создании пользователя помимо имени пользователя и пароля создается
    токен для авторизации, который возвращается пользователю вместе с его
    именем.

    """
    token = serializers.SerializerMethodField('get_token')

    class Meta:
        model = User
        fields = ('username', 'password', 'token')
        extra_kwargs = ({'password': {'write_only': True}})

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.save()
        return user

    def get_token(self, user):
        """Создание токена при создании пользователя.
        Отображение токена при просмотре списка пользователей (только
        администраторы).

        """
        try:
            return Token.objects.create(user=user).key
        except:
            return Token.objects.get(user=user).key
