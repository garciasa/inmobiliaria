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
'''
    @classmethod
    def create(cls,form):
        return cls(fecha_insert=datetime.date(2013,01,01),
                tipo=form.cleaned_data['tipo'],
                provincia=form.cleaned_data['provincia'],
                localidad=form.cleaned_data['localidad'],
                direccion = form.cleaned_data['direccion'],
                zona=form.cleaned_data['zona'],
                banos=form.cleaned_data['banos'],
                habitaciones=form.cleaned_data['habitaciones'],
                metros_casa=form.cleaned_data['metros_casa'],
                contenido=form.cleaned_data['contenido'],
                precio = form.cleaned_data['precio'],
                activo=form.cleaned_data['activo'],
                visitas = random.randrange(1,43),
                )
'''

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


