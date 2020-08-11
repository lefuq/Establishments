from rest_framework import permissions
from rest_framework.exceptions import NotAuthenticated
from apps.catering.models.establishments import Establishment

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class IsEstOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        est_id = int(request.POST.get('place'))
        place = Establishment.objects.get(id=est_id)
        return place.owner == request.user

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
