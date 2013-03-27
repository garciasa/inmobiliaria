# -*- coding: utf-8 -*-
from django import forms

CHOICES_SEARCH = ((1,'Alquiler'),(2,'Venta'))
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
    metros_jardin = forms.IntegerField(label='Metros Jardin')
    habitaciones = forms.IntegerField(label='Habitaciones', required=True)
    banos = forms.IntegerField(label='Baños',required=True)
    contenido = forms.CharField(label='Descripcion', widget=forms.Textarea, required=True)
    activo = forms.BooleanField(label='Activo', initial='True')

class ImageForm(forms.Form):
    descripcion = forms.CharField(label='Descripcion', required=True)
    fichero = forms.FileField(label='Foto', required=True)