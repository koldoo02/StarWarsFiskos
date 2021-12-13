from django.contrib import admin

from StarWarsApp.models import Pelicula, Personaje, Raza

# Register your models here.
admin.site.register(Pelicula)
admin.site.register(Personaje)
admin.site.register(Raza)