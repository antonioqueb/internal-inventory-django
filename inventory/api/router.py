from rest_framework.routers import DefaultRouter

from inventory.api.views import ArticulosViewSet

router = DefaultRouter()
router.register(prefix='inventario', viewset=ArticulosViewSet, basename='inventario')


