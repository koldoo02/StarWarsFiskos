from typing import Text
from django.db import models

# Create your models here.
class Pelicula(models.Model):
 nombre = models.CharField(max_length=40)
 año = models.IntegerField()


 def __str__(self):
     return f"id={self.id}, nombre = {self.nombre}, año = {self.año}"

   
class Raza(models.Model):
 nombre = models.CharField(max_length=40)
 mundo = models.CharField(max_length=40)



 def __str__(self):
     return f"id={self.id}, nombre = {self.nombre}, mundo = {self.mundo}"


class Personaje(models.Model):
 nombre = models.CharField(max_length=40)
 raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
 altura = models.FloatField()
 actor = models.CharField(max_length=40)
 peliculas = models.ManyToManyField(Pelicula)
 image = models.ImageField(upload_to='static/images/BD', default = 'default.jpg')
 descripcion = models.CharField(max_length=3000)

 def __str__(self):
     return f"id={self.id}, nombre = {self.nombre}, raza = {self.raza}, altura = {self.altura}, peliculas = {self.peliculas}, img = {self.image}"


 

 