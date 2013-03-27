import datetime
from django.db import models


TIPO_INMUEBLE = (
    ('A','Alquiler'),
    ('V','Venta'),
)


class Inmueble(models.Model):
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

    def __unicode__(self):
        return u'%s - %s' % (self.id, self.descripcion)

    @classmethod
    def create(cls,form):
        return cls(fecha_insert=datetime.date(2013,01,01),
                descripcion=form.cleaned_data['titulo'],
                tipo=form.cleaned_data['tipo'],
                provincia=form.cleaned_data['provincia'],
                localidad=form.cleaned_data['localidad'],
                zona=form.cleaned_data['zona'],
                banos=form.cleaned_data['banos'],
                habitaciones=form.cleaned_data['habitaciones'],
                metros_casa=form.cleaned_data['metros_casa'],
                metros_jardin=form.cleaned_data['metros_jardin'],
                contenido=form.cleaned_data['contenido'],
                activo=form.cleaned_data['activo'],
                )

class Imagen(models.Model):
    ruta = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    inmueble = models.ForeignKey(Inmueble ,verbose_name=u'Id del Inmueble al que pertenece')
    
    def __unicode__(self):
        return u'%s - %s' % (self.id, self.nombre)

    @classmethod
    def create(cls,form):
        return cls(ruta='static/',
                nombre=form.cleaned_data['fichero'],
                descripcion=form.cleaned_data['descripcion'],
                )


