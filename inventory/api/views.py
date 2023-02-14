from rest_framework.viewsets import ModelViewSet

from inventory.models import Articulo
from inventory.api.serializers import ArticuloSerializer

class ArticulosViewSet(ModelViewSet):
    serializer_class = ArticuloSerializer
    queryset = Articulo.objects.all()

