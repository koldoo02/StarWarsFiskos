from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from .models import Pelicula,Raza,Personaje
# Create your views here.

def home(request):
    peliculas= Pelicula.objects.order_by('id')
    razas= Raza.objects.order_by('id')
    personajes= Personaje.objects.order_by('id') 
    
    return render(request,'index.html',{'lista_peliculas' : peliculas,'lista_razas' : razas,'lista_personajes' : personajes})


def buscarPersonajesRaza(request, id_raza):
    Peliculas= Pelicula.objects.order_by('id')
    razas= Raza.objects.order_by('id')
    razaSeleccionada = Raza.objects.filter(pk = id_raza)
    personajes= Personaje.objects.filter(raza__in = razaSeleccionada)
    
    return render(request,'buscarPersonajes.html',{'lista_peliculas' : Peliculas,'lista_razas' : razas,'lista_personajes' : personajes})

def buscarPersonajesRazaYPelicula(request, id_raza, id_pelicula):
    Peliculas= Pelicula.objects.order_by('id')
    peliculaSeleccionada = Pelicula.objects.filter(pk = id_pelicula)
    razas= Raza.objects.order_by('id')
    razaSeleccionada = Raza.objects.filter(pk = id_raza)
    personajes= Personaje.objects.filter(raza__in = razaSeleccionada, peliculas__in = peliculaSeleccionada)

    return render(request,'buscarPersonajes.html',{'lista_peliculas' : Peliculas,'lista_razas' : razas,'lista_personajes' : personajes})


def test1(request):
    peliculas= Pelicula.objects.order_by('id')
    razas= Raza.objects.order_by('id')
    personajes= Personaje.objects.all()
    return render(request,"test1.html",{'lista_peliculas' : peliculas,'lista_razas' : razas,'lista_personajes' : personajes})

def test2(request):
    results=request.GET['peliculaseleccionada']
    return render(request,"test2.html",{'peliculaseleccionada':results})


class PersonajeDetailView(DetailView):
    model = Personaje
    template_name = 'detallesPersonaje.html'

