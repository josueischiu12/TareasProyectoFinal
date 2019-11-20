from rest_framework import routers
from tareas.viewsets import TareaViewSet
from registration.viewsets import UserViewSet, GroupViewSet

router = routers.DefaultRouter()

router.register(r'tarea', TareaViewSet)
router.register(r'user', UserViewSet)
router.register(r'group', GroupViewSet)