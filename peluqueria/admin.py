"""Panel de administración personalizado para Coquettos."""

from django.contrib import admin
from .models import Servicio, ClientePeludo, Resena, CitaReserva, MensajeContacto


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'icono', 'precio_desde', 'destacado', 'orden']
    list_editable = ['destacado', 'orden', 'precio_desde']
    ordering = ['orden']


@admin.register(ClientePeludo)
class ClientePeludoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'raza', 'es_estrella', 'orden']
    list_editable = ['es_estrella', 'orden']
    ordering = ['orden']


@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ['nombre_cliente', 'puntuacion', 'fecha', 'visible']
    list_editable = ['visible']
    list_filter = ['puntuacion', 'visible']
    ordering = ['-fecha']


@admin.register(CitaReserva)
class CitaReservaAdmin(admin.ModelAdmin):
    list_display = ['nombre_mascota', 'nombre_dueno', 'telefono', 'servicio', 'fecha_hora', 'estado']
    list_editable = ['estado']
    list_filter = ['estado', 'servicio']
    ordering = ['fecha_hora']
    readonly_fields = ['creada_en']


@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'telefono', 'creado_en', 'leido']
    list_editable = ['leido']
    ordering = ['-creado_en']
    readonly_fields = ['creado_en']
