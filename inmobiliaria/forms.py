# -*- coding: utf-8 -*-
from django import forms
from captcha.fields import CaptchaField
from inmobiliaria.models import Inmueble, Imagen
from django.forms import ModelForm
from haystack.forms import SearchForm
from haystack.query import SearchQuerySet
import logging
import pdb


CHOICES_SEARCH = (('A','Alquiler'),('V','Venta'))
CHOICES_PROVINCIA = ((1,'Madrid'),(2,'Otros'))

logger = logging.getLogger('django')


class InmuebleSearchForm(SearchForm):
    tipo = forms.ChoiceField(label='Tipo',choices=CHOICES_SEARCH, required=True)
    provincia = forms.ChoiceField(label='Provincia', choices=CHOICES_PROVINCIA,required=True)
    habitaciones = forms.IntegerField(label='Habitaciones',required=False)

    def search(self):
        if not self.is_valid():
            return self.no_query_found()

        if not self.cleaned_data.get('q'):
            # No query: return all data
            #logger.debug('paso por aqui')
            #pdb.set_trace()
            sqs = SearchQuerySet().all()

            logger.debug(vars(sqs))
        else:
            sqs = SearchQuerySet().auto_query(self.cleaned_data['q'])            
        
        if self.cleaned_data['habitaciones']:
            sqs = sqs.filter(habitaciones__eq=self.cleaned_data['habitaciones']) 
        
        if self.cleaned_data['provincia']:
            #logger.debug(self.cleaned_data['provincia'])
            #pdb.set_trace()
            d = dict(CHOICES_PROVINCIA)
            sqs = sqs.filter(provincia__eq=d[int(self.cleaned_data['provincia'])])
        
        if self.cleaned_data['tipo']:
            #logger.debug(self.cleaned_data['provincia'])
            #pdb.set_trace()
            d = dict(CHOICES_SEARCH)
            sqs = sqs.filter(tipo__eq=d[self.cleaned_data['tipo']])


        return sqs

class AddForm(ModelForm):
    class Meta:
        model = Inmueble
        exclude = ('fecha_insert','visitas')

    #fecha_insert = forms.DateField(label='Fecha Alta',required=False)
    #titulo = forms.CharField(label='Titulo',required=True)
    #tipo = forms.ChoiceField(label='Tipo',choices=CHOICES_SEARCH, required=True)
    #provincia = forms.ChoiceField(label='Provincia', choices=CHOICES_PROVINCIA,required=True)
    #localidad = forms.CharField(label='Localidad', required=True)
    #zona = forms.CharField(label='Zona', required=True)
    #direccion = forms.CharField(label='Direccion', required=True)
    #metros_casa = forms.IntegerField(label='Metros', required=True)
    #habitaciones = forms.IntegerField(label='Habitaciones', required=True)
    #banos = forms.IntegerField(label='Baños',required=True)
    #contenido = forms.CharField(label='Descripcion', widget=forms.Textarea, required=True)
    #precio = forms.IntegerField(label='Precio',min_value=0, max_value=999999999, required=True)
    #activo = forms.BooleanField(label='Activo', initial='True',required=False)

class ImageForm(ModelForm):
    class Meta:
        model = Imagen
        exclude = ('nombre','ruta','inmueble')

    #descripcion = forms.CharField(label='Descripcion', required=True)
    fichero = forms.ImageField(label='Foto', required=True)


class ContactForm(forms.Form):
    nombre = forms.CharField(required=True)
    email = forms.EmailField(min_length=6,required=True)
    mensaje = forms.CharField(widget=forms.Textarea,required=True)
    captcha = CaptchaField()

class ActionForm(forms.Form):
    operacion = forms.CharField(widget=forms.HiddenInput(),required=True)
    item = forms.CharField(widget=forms.HiddenInput(),required=True, max_length=3)

class EnviarForm(forms.Form):
    to = forms.EmailField(label='Para',required=True)
    subject = forms.CharField(label='Asunto',max_length=50,required=True) 
    body = forms.CharField(label='Cuerpo', widget=forms.Textarea,required=True)
