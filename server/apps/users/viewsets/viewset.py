from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from django.contrib.auth.models import User
from apps.main.permissions.permissions import IsNewUser
from drf_yasg.utils import swagger_auto_schema

from rest_framework.response import Response
from drf_yasg import openapi

from apps.users.serializers.serializer import UserSerializer

class UserViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):
    """Viewset пользователей. Просмотр списка пользователей разрешен только
    администраторам. В ином случае разрешено только создание.

    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsNewUser]

    @swagger_auto_schema(
        responses={200: openapi.Response(
            'Выводит на экран список пользователей и их токен',
            openapi.Schema(
                title='Пользователь',
                type=openapi.TYPE_OBJECT,
                properties={
                    'username': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        title='Имя пользователя',
                    ),
                    'token': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        title='Токен пользователя',
                    ),
                }
            )
        )
        },
    )
    def list(request, pk):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        responses={201: openapi.Response(
            'Создание пользователя и возвращает его имя и токен',
            openapi.Schema(
                title='Пользователь',
                type=openapi.TYPE_OBJECT,
                properties={
                    'username': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        title='Имя пользователя',
                    ),
                    'token': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        title='Токен пользователя',
                    ),
                }
            )
        )
        },
    )
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
