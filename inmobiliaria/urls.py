from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

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
    url(r'^inmuebles','inmobiliaria.views.inmuebles',name='inmuebles'),
    url(r'^contacto','inmobiliaria.views.contacto',name='contacto'),
    url(r'^private/add','inmobiliaria.views.addInmueble',name='addInmueble'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'inmobiliaria.views.logout_page'),
)
