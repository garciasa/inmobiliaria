#mis vistas
import os
import logging
from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.core.context_processors import csrf
from django.template import RequestContext
from django.forms.formsets import formset_factory, BaseFormSet
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from inmobiliaria.forms import SearchForm, AddForm, ImageForm
from inmobiliaria.models import Inmueble, Imagen

logger = logging.getLogger('django')

def home(request):
    return render_to_response('home_inmo.html',context_instance=RequestContext(request))

def nosotros(request):
    return render(request,'about_inmo.html',context_instance=RequestContext(request))

def alquiler(request):
    return render_to_response('alquiler_inmo.html',context_instance=RequestContext(request))

def venta(request):
    return render_to_response('venta_inmo.html',context_instance=RequestContext(request))

def compra(request):
    return render_to_response('compra_inmo.html',context_instance=RequestContext(request))

def inmuebles(request):
    form = SearchForm();
    return render_to_response('inmuebles_inmo.html',{'form':form},context_instance=RequestContext(request))

def contacto(request):
    return render_to_response('contact_inmo.html',context_instance=RequestContext(request))

@login_required
def addInmueble(request):
    # This class is used to make empty formset forms required
    # See http://stackoverflow.com/questions/2406537/django-formsets-make-first-required/4951032#4951032
    class RequiredFormSet(BaseFormSet):
        def __init__(self, *args, **kwargs):
            super(RequiredFormSet, self).__init__(*args, **kwargs)
            for form in self.forms:
                form.empty_permitted = False
    
    ImageFormSet = formset_factory(ImageForm, max_num=5, formset=RequiredFormSet)
    if request.method == 'POST':
        #Guardamos todo esto...
        inmuebleForm = AddForm(request.POST)
        imageFormSet = ImageFormSet(request.POST, request.FILES)
        
        if inmuebleForm.is_valid() and imageFormSet.is_valid():
            casa = Inmueble.create(inmuebleForm)
            #logger.debug(vars(casa))
            casa.save()
            #logger.debug(vars())
            cont = 1
            for f in imageFormSet.forms:
                ruta,nombre = manage_file(f.cleaned_data['fichero'],casa.id, cont)
                img_casa = Imagen.create(f)
                img_casa.ruta = ruta
                img_casa.nombre = nombre
                img_casa.inmueble = casa
                img_casa.save()
                cont+=1

            return render_to_response('home_inmo.html',context_instance=RequestContext(request))
        else:
            data = {'inmueble_form':inmuebleForm,
                 'image_formset':ImageFormSet,
                }
    else:
        inmuebleForm = AddForm();
        data = {'inmueble_form':inmuebleForm,
             'image_formset':ImageFormSet,
             }
        
    data.update(csrf(request))
    return render_to_response('admin/add_inmo.html',data)

def manage_file(f,_id,_cont):
    #Guardamos archivo
    nombre = 'img-'+str(_id)+'-'+str(_cont)+'.jpg'
    ruta = os.path.join(settings.SITE_ROOT, 'static/img/casas/')
    with open(ruta+nombre
        , 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    logger.debug('Guardando fichero....')
    return ('static/img/casas/',nombre)
    
def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')