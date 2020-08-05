from rest_framework import routers

from apps.test.viewsets import TestViewSet
from apps.users.viewsets.viewset import UserViewSet
from apps.catering.viewsets.estviewset import EstViewSet
from apps.catering.viewsets.ingrviewset import IngrViewSet
from apps.catering.viewsets.dishviewset import DishViewSet

router = routers.DefaultRouter()
router.register('test', TestViewSet, basename='test')
router.register('users', UserViewSet, basename='users')
router.register('establishments', EstViewSet, basename='establishments')
router.register('ingredients', IngrViewSet, basename='ingredients')
router.register('dishes', DishViewSet, basename='dishes')
