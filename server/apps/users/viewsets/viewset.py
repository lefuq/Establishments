from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from django.contrib.auth.models import User
from apps.main.permissions.permissions import IsNewUser

from apps.users.serializers.serializer import UserSerializer

class UserViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):
    """Viewset пользователей. Просмотр списка пользователей разрешен только
    администраторам. В ином случае разрешено только создание.

    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsNewUser]
