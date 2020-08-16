from rest_framework import permissions
from rest_framework.exceptions import NotAuthenticated
from apps.catering.models.establishments import Establishment

class IsOwnerOrReadOnly(permissions.BasePermission):
    """Проверка пользователя на то, является ли он владельцем заведения при
    редактировании заведения.

    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class IsEstOwnerOrReadOnly(permissions.BasePermission):
    """Проверка пользователя на то, является ли он владельцем заведения при
    создании и редактировании блюда.

    """
    def has_permission(self, request, view):
        """Проверка пользователя на владение заведением, в которое он добавляет
        блюдо посредством POST-запроса.
        Проверка пользователя на владение блюдом при его редактировании.

        """
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            try:
                est_id = int(request.POST.get('place'))
                place = Establishment.objects.get(id=est_id)
            except:
                return 'Указан некорректный id заведения при создании блюда.'
            return place.owner == request.user

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.place.owner == request.user

class IsNewUser(permissions.BasePermission):
    """Проверка пользователя на то, является ли он администратором для
    просмотра списка пользователей и их токенов. В ином случае разрешено
    только создание пользователя.

    """
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return request.user.is_staff
