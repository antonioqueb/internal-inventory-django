from io import BytesIO
from django.core.files import File
import qrcode
from django.db import models


class Articulo(models.Model):
    folio = models.IntegerField(default=0)
    identificador = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    ubicacion = models.CharField(max_length=255)
    marca = models.CharField(max_length=255, blank=True)
    modelo = models.CharField(max_length=255, blank=True)
    numero_serie = models.CharField(max_length=255)
    estado = models.CharField(max_length=255, blank=True)
    resguardante = models.CharField(max_length=255)
    fecha_adquisicion = models.DateField(blank=True)
    categoria = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='articulos', blank=True)
    fecha_revision = models.DateField(blank=True)
    frecuencia_revision = models.IntegerField(blank=True)
    historial_mantenimiento = models.TextField(blank=True)
    historial_uso = models.TextField(blank=True)
    qr_code_image = models.ImageField(upload_to='articulos', blank=True)




def generate_qr_code(instance_id):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(str(instance_id))
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img


def save_qr_code(sender, instance, **kwargs):
    if not instance.qr_code_image:
        img = generate_qr_code(instance.id)
        fname = f"qr_code_{instance.id}.png"
        buffer = BytesIO()
        img.save(buffer, 'PNG')
        instance.qr_code_image.save(fname, File(buffer), save=False)
        instance.save()



