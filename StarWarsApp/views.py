from django.shortcuts import render
from django.http import HttpResponse
from .models import Pelicula,Raza,Personaje
# Create your views here.

def index(request):
    peliculas= Pelicula.objects.order_by('id').all()
    razas= Raza.objects.order_by('id').all()
    personajes=Personaje.objects.all()

    return render(request,"index.html",{'lista_peliculas' : peliculas,'lista_razas' : razas,'lista_personajes' : personajes})

def buscarPersonajes(request):
    results=request.GET['razaseleccionada']
    results2=request.GET['peliculaseleccionada'] 

    peliculas= Pelicula.objects.order_by('id').all()
    razas= Raza.objects.order_by('id').all()
    personajes=Personaje.objects.all()

    return render(request,"buscarPersonajes.html",{'razaseleccionada':results,'peliculaseleccionada':results2,'lista_peliculas' : peliculas,'lista_razas' : razas,'lista_personajes' : personajes})



    
def test1(request):
    peliculas= Pelicula.objects.order_by('id').all()
    razas= Raza.objects.order_by('id').all()
    personajes=Personaje.objects.all()

    return render(request,"test1.html",{'lista_peliculas' : peliculas,'lista_razas' : razas,'lista_personajes' : personajes})

def test2(request):
    results=request.GET['razaseleccionada']
    results2=request.GET['peliculaseleccionada'] 
    return render(request,"test2.html",{'razaseleccionada':results,'peliculaseleccionada':results2})


