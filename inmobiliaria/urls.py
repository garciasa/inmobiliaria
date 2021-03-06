from django.conf.urls import patterns, include, url
from haystack.query import SearchQuerySet
from haystack.views import SearchView
from inmobiliaria.forms import InmuebleSearchForm
from inmobiliaria.views import InmueblesSearchView


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

sqs = SearchQuerySet()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'inmobiliaria.views.home', name='home'),
    # url(r'^inmobiliaria/', include('inmobiliaria.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^gestiona/', include(admin.site.urls)),
    url(r'^$','inmobiliaria.views.home',name='home'),
    url(r'^nosotros','inmobiliaria.views.nosotros',name='nosotros'),
    url(r'^alquiler','inmobiliaria.views.alquiler',name='alquiler'),
    url(r'^venta','inmobiliaria.views.venta',name='venta'),
    url(r'^compra','inmobiliaria.views.compra',name='compra'),
    url(r'^inmuebles/(\d+)','inmobiliaria.views.descripcion_inmueble',name='inmuebles'),
    url(r'^inmuebles','inmobiliaria.views.inmuebles',name='inmuebles'),
    url(r'^contacto','inmobiliaria.views.contacto',name='contacto'),
    url(r'^search/', InmueblesSearchView(
        template='search/search.html',
        searchqueryset=sqs,
        form_class=InmuebleSearchForm
    ), name='haystack_search'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^private/$','inmobiliaria.views.listInmueble',name='listInmueble'),
    url(r'^private/add/$','inmobiliaria.views.addInmueble',name='addInmueble'),
    url(r'^private/mod/(\d+)?','inmobiliaria.views.modInmueble',name='modInmueble'),
    url(r'^private/ver/(\d+)?','inmobiliaria.views.verInmueble',name='verInmueble'),
    url(r'^private/enviar/(\d+)?','inmobiliaria.views.enviarInmueble',name='enviarInmueble'),
    url(r'^private/login/$', 'django.contrib.auth.views.login'),
    url(r'^private/logout/$', 'inmobiliaria.views.logout_page',name='logout'),
)
