import datetime
import random
from django.db import models


TIPO_INMUEBLE = (
    ('A','Alquiler'),
    ('V','Venta'),
)

CHOICES_PROVINCIA = (
    ('1','Madrid'),
    ('2','Otros'),
)


class Inmueble(models.Model):
    fecha_insert = models.DateField(blank=True,null=True)
    descripcion = models.CharField(max_length=50,blank=True)
    tipo = models.CharField(max_length=2,choices=TIPO_INMUEBLE,default='Alquiler')
    provincia = models.CharField(max_length=30,choices=CHOICES_PROVINCIA, default='Madrid')
    localidad = models.CharField(max_length=40)
    zona = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    banos = models.IntegerField()
    habitaciones = models.IntegerField()
    metros_casa = models.IntegerField()
    contenido = models.TextField(max_length=250)
    precio = models.PositiveIntegerField()
    activo = models.BooleanField()
    visitas = models.IntegerField(blank=True,null=True)


    def __unicode__(self):
        return u'%s - %s' % (self.id, self.descripcion)

    def get_absolute_url(self):
        return "/inmuebles/%i/" % (self.id)


class Imagen(models.Model):
    ruta = models.CharField(max_length=50, blank=True)
    nombre = models.CharField(max_length=50, blank=True)
    descripcion = models.CharField(max_length=50)
    inmueble = models.ForeignKey(Inmueble ,verbose_name=u'Id del Inmueble al que pertenece', blank=True)
    
    def __unicode__(self):
        return u'%s - %s' % (self.id, self.nombre)

    @classmethod
    def create(cls,form):
        return cls(ruta='static/',
                nombre=form.cleaned_data['fichero'],
                descripcion=form.cleaned_data['descripcion'],
                )


