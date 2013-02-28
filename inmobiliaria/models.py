from django.db import models

class Imagen(models.Model):
    ruta = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    prueba = models.CharField(max_length=50)


class Inmueble(models.Model):
    TIPO_INMUEBLE = (
        ('A','Alquiler'),
        ('V','Venta'),
    )
    fecha_insert = models.DateField()
    descripcion = models.CharField(max_length=50)
    tipo = models.CharField(max_length=2,choices=TIPO_INMUEBLE)
    provincia = models.CharField(max_length=30)
    localidad = models.CharField(max_length=40)
    zona = models.CharField(max_length=50)
    banos = models.IntegerField()
    habitaciones = models.IntegerField()
    metros_casa = models.IntegerField()
    metros_jardin = models.IntegerField()
    contenido = models.CharField(max_length=250)
    activo = models.BooleanField()
    Imagenes = models.ForeignKey(Imagen, verbose_name=u'Lista de Imagenes')
