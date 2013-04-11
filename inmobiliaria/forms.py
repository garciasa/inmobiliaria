# -*- coding: utf-8 -*-
from django import forms
from captcha.fields import CaptchaField

CHOICES_SEARCH = (('A','Alquiler'),('V','Venta'))
CHOICES_PROVINCIA = ((1,'Madrid'),(2,'Otros'))

class SearchForm(forms.Form):
    tipo = forms.ChoiceField(label='Tipo',choices=CHOICES_SEARCH, required=True)
    provincia = forms.ChoiceField(label='Provincia', choices=CHOICES_PROVINCIA,required=True)
    habitaciones = forms.CharField(label='Habitaciones',required=True)

class AddForm(forms.Form):
    fecha_insert = forms.DateField(label='Fecha Alta',required=False  )
    titulo = forms.CharField(label='Titulo',required=True)
    tipo = forms.ChoiceField(label='Tipo',choices=CHOICES_SEARCH, required=True)
    provincia = forms.ChoiceField(label='Provincia', choices=CHOICES_PROVINCIA,required=True)
    localidad = forms.CharField(label='Localidad', required=True)
    zona = forms.CharField(label='Zona', required=True)
    descripcion = forms.CharField(label='Titulo', required=True)
    metros_casa = forms.IntegerField(label='Metros', required=True)
    habitaciones = forms.IntegerField(label='Habitaciones', required=True)
    banos = forms.IntegerField(label='Baños',required=True)
    contenido = forms.CharField(label='Descripcion', widget=forms.Textarea, required=True)
    precio = forms.IntegerField(label='Precio',min_value=0, max_value=999999999, required=True)
    activo = forms.BooleanField(label='Activo', initial='True')

class ImageForm(forms.Form):
    descripcion = forms.CharField(label='Descripcion', required=True)
    fichero = forms.ImageField(label='Foto', required=True)

class ContactForm(forms.Form):
    nombre = forms.CharField(required=True)
    email = forms.EmailField(min_length=6,required=True)
    mensaje = forms.CharField(widget=forms.Textarea,required=True)
    captcha = CaptchaField()
