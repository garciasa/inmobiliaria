from django import forms

CHOICES_SEARCH = ((1,'Alquiler'),(2,'Venta'))
CHOICES_PROVINCIA = ((1,'Madrid'),(2,'Otros'))

class SearchForm(forms.Form):
    tipo = forms.ChoiceField(label='Tipo',choices=CHOICES_SEARCH, required=True)
    provincia = forms.ChoiceField(label='Provincia', choices=CHOICES_PROVINCIA,required=True)
    habitaciones = forms.CharField(label='Habitaciones',required=True)