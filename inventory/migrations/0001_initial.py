# Generated by Django 4.1.5 on 2023-02-14 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio', models.IntegerField(default=0)),
                ('identificador', models.CharField(max_length=255)),
                ('descripcion', models.TextField(blank=True)),
                ('ubicacion', models.CharField(max_length=255)),
                ('marca', models.CharField(blank=True, max_length=255)),
                ('modelo', models.CharField(blank=True, max_length=255)),
                ('numero_serie', models.CharField(max_length=255)),
                ('estado', models.CharField(blank=True, max_length=255)),
                ('resguardante', models.CharField(max_length=255)),
                ('fecha_adquisicion', models.DateField(blank=True)),
                ('categoria', models.CharField(max_length=255)),
                ('imagen', models.ImageField(blank=True, upload_to='articulos')),
                ('fecha_revision', models.DateField(blank=True)),
                ('frecuencia_revision', models.IntegerField(blank=True)),
                ('historial_mantenimiento', models.TextField(blank=True)),
                ('historial_uso', models.TextField(blank=True)),
                ('qr_code_image', models.ImageField(blank=True, upload_to='articulos')),
            ],
        ),
    ]