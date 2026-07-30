"""URLs para la app peluqueria de Coquettos."""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('servicios/', views.servicios, name='servicios'),
    path('galeria/', views.galeria, name='galeria'),
    path('cita/', views.cita, name='cita'),
    path('cita/confirmada/', views.cita_confirmada, name='cita_confirmada'),
    path('contacto/', views.contacto, name='contacto'),
]
