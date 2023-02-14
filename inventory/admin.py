from django.contrib import admin
from inventory.models import Articulo # Register your models here.

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('folio', 'identificador', 'descripcion', 'ubicacion', 'marca', 'modelo', 'numero_serie', 'estado', 'resguardante', 'fecha_adquisicion', 'categoria', 'imagen', 'fecha_revision', 'frecuencia_revision', 'historial_mantenimiento', 'historial_uso', 'qr_code_image')
    list_filter = ('folio', 'identificador', 'descripcion', 'ubicacion', 'marca', 'modelo', 'numero_serie', 'estado', 'resguardante', 'fecha_adquisicion', 'categoria', 'imagen', 'fecha_revision', 'frecuencia_revision', 'historial_mantenimiento', 'historial_uso', 'qr_code_image')
    search_fields = ('folio', 'identificador', 'descripcion', 'ubicacion', 'marca', 'modelo', 'numero_serie', 'estado', 'resguardante', 'fecha_adquisicion', 'categoria', 'imagen', 'fecha_revision', 'frecuencia_revision', 'historial_mantenimiento', 'historial_uso', 'qr_code_image')
    

    def __str__(self):
        return self.nombre

    
