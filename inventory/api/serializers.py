from rest_framework.serializers import ModelSerializer
from inventory.models import Articulo

class ArticuloSerializer(ModelSerializer):
    class Meta:
        model = Articulo
        fields = ('id', 'folio', 'identificador', 'descripcion', 'ubicacion', 'marca', 'modelo', 'numero_serie', 'estado', 'resguardante', 'fecha_adquisicion', 'categoria', 'imagen', 'fecha_revision', 'frecuencia_revision', 'historial_mantenimiento', 'historial_uso', 'qr_code_image')