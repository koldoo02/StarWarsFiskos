
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('buscarPersonajes/<int:id_raza>',views.buscarPersonajesRaza, name = 'buscarPersonajesRaza'),
   path('buscarPersonajes/<int:id_raza>/<int:id_pelicula>', views.buscarPersonajesRazaYPelicula, name = 'buscarPersonajesRazaYPelicula'),
   path('test1',views.test1,name='test1'),
   path('test2',views.test2,name='test2')

]
