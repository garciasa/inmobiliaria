from haystack import indexes
from inmobiliaria.models import Inmueble

class InmuebleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    descripcion = indexes.CharField(model_attr='descripcion')
    tipo = indexes.CharField(model_attr='tipo',faceted=True)
    provincia = indexes.CharField(model_attr='provincia',faceted=True)
    localidad = indexes.CharField(model_attr='localidad',faceted=True)
    zona = indexes.CharField(model_attr='zona',faceted=True)
    banos = indexes.CharField(model_attr='banos',faceted=True)
    habitaciones = indexes.CharField(model_attr='habitaciones',faceted=True)
    contenido = indexes.CharField(model_attr='contenido')


    def get_model(self):
        return Inmueble

    def prepare_tipo(self,obj):
        return obj.get_tipo_display()

    def prepare_provincia(self,obj):
        return obj.get_provincia_display()

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
        #return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())