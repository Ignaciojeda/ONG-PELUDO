from django.shortcuts import render

# Create your views here.
#def -> crear funcion

def index(request):
    contexto={}
    return render(request, 'index.html',contexto)