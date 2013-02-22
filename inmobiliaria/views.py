#mis vistas
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from inmobiliaria.forms import SearchForm

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