#mis vistas
import os
import logging
from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.core.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    casas_list = Inmueble.objects.all()
    paginator = Paginator(casas_list,3)

    page = request.GET.get('page')
    try:
        casas = paginator.page(page)
    except PageNotAnInteger:
        casas = paginator.page(1)
    except EmptyPage:
        casas = paginator.page(paginator.num_pages)

    return render_to_response('inmuebles_inmo.html',{'form':form,
                                                     'casas':casas},context_instance=RequestContext(request))

def descripcion_inmueble(request,id):
    if request.method == 'GET':
        logger.debug(id)
        try:
            c = Inmueble.objects.get(pk=id)
        except Inmueble.DoesNotExist:
            c = None
        
        if c:            
            #aqui tenemos que mandar a la vista correspondiente para mostrar la casa con todos los datos... 
            return render_to_response('home_inmo.html',context_instance=RequestContext(request))
        else:
            return inmuebles(request)



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
   
    if request.method == 'POST':
        #Guardamos todo esto...
        
        ImageFormSet = formset_factory(ImageForm, max_num=5, formset=RequiredFormSet)

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
                img_casa.nombre = nombre[:-4]
                img_casa.inmueble = casa
                img_casa.save()
                cont+=1
            
            inmuebleForm = AddForm();
            data = {'inmueble_form':inmuebleForm,
             'image_formset':ImageFormSet,
             'respuesta' : 'ok',
             }        
            data.update(csrf(request))
            return render_to_response('gestiona/add_inmo.html',data)  
        else:
            data = {
                    'inmueble_form':inmuebleForm,
                    'image_formset':imageFormSet,
                    }
    else:
        inmuebleForm = AddForm();
        imageFormSet = formset_factory(ImageForm, max_num=5, formset=RequiredFormSet)
        data = {'inmueble_form':inmuebleForm,
             'image_formset':imageFormSet,
             'respuesta' : '',
             }
        
    data.update(csrf(request))
    return render_to_response('gestiona/add_inmo.html',data)

def manage_file(f,_id,_cont):
    ''' Guardamos archivo
        y convertimos al tamano deseado.
        Tambien hacemos un thumbnail de todas.'''
    from PIL import Image

    image = add_watermark(f,'inversioneslamoraleja.com')
    thumbnailSize = (426,318)
    normalSize = (650,488)


    nombre = 'img-'+str(_id)+'-'+str(_cont)+'.png'
    nombreThumb = 'img-'+str(_id)+'-'+str(_cont)+'-thumbnail.png'
    ruta = os.path.join(settings.SITE_ROOT, 'static/img/casas/')
    
    image.thumbnail(normalSize, Image.ANTIALIAS)
    image.save(ruta+nombre,'PNG',optimized=True)  

    image.thumbnail(thumbnailSize, Image.ANTIALIAS)    
    image.save(ruta+nombreThumb,'PNG',optimized=True)  

    logger.debug('Guardando fichero....')
    return ('static/img/casas/',nombre)

def add_watermark(image, text,angle=23,opacity=0.5):
    from PIL import Image, ImageDraw, ImageFont, ImageEnhance
    #TODO: Cambiar en produccion, esto para que la encuentre en osx
    FONT = '/Library/Fonts/Arial Black.ttf'
    img = Image.open(image).convert('RGB')
    watermark = Image.new('RGBA', img.size, (0,0,0,0))
    size = 2
    n_font = ImageFont.truetype(FONT, size)
    n_width, n_height = n_font.getsize(text)
    while (n_width+n_height < watermark.size[0]):
        size += 2
        n_font = ImageFont.truetype(FONT, size)
        n_width, n_height = n_font.getsize(text)
    draw = ImageDraw.Draw(watermark, 'RGBA')
    draw.text(((watermark.size[0] - n_width) / 2,
              (watermark.size[1] - n_height) / 2),
              text, font=n_font)
    watermark = watermark.rotate(angle,Image.BICUBIC)
    alpha = watermark.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    watermark.putalpha(alpha)
    return Image.composite(watermark, img, watermark)


def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')