from rest_framework import routers

from apps.test.viewsets import TestViewSet
from apps.users.viewsets.viewset import UserViewSet
from apps.catering.viewsets.viewset import EstViewSet


router = routers.DefaultRouter()
router.register('test', TestViewSet, basename='test')
router.register('users', UserViewSet, basename='users')
router.register('establishments', EstViewSet, basename='establishments')
