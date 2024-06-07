from django.shortcuts import render
from .models import *
# Create your views here.
#def -> crear funcion

def index(request):
    gatos=Gato.objects.all();
    contexto={"Gatitos":gatos}
    return render(request, 'index.html',contexto)

def Perros(request):
    contexto={}
    return render(request, 'Perros.html',contexto)

def Gatos(request):
    contexto={}
    return render(request, 'Gatos.html',contexto)

def Contacto(request):
    contexto={}
    return render(request, 'Contacto.html',contexto)

