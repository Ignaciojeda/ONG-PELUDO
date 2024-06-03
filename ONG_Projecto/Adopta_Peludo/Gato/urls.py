from django.urls import path
from . import views

#Crear lista con url

urlpatterns = [
    path('index', views.index, name='index'), #index es el nombre de la funcion en vistas
]