
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name='home'),
   path('buscarPersonajes',views.buscarPersonajes, name = 'buscarPersonajes'),
   path('test1',views.test1,name='test1'),
   path('test2',views.test2,name='test2')

]
