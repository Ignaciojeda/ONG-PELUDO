from django.urls import path
from . import views

urlpatterns =  [
    path('',views.index,name='index'),
    path('Perros/', views.Perros,name='Perros'),
    path('Gatos/', views.Gatos,name='Gatos'),
    path('Contacto/',views.Contacto,name='Contacto'),
    path('mascota/',views.mascota,name='mascota'),
    path('administracion/',views.Administrador,name='Administrador'),
    path('agregarMascota',views.agregarMascota,name='agregarMascota'),
    path('encontrarMascota/<str:pk>',views.encontrarMascota,name='encontrarMascota'),
    path('modificarMascota',views.modificarMascota,name='modificarMascota'),
    path('eliminarMascota/<str:pk>',views.eliminarMascota,name='eliminarMascota'),
 
]