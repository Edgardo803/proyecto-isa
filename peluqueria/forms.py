"""Formularios para Coquettos Peluquería Canina."""

from django import forms
from .models import CitaReserva, MensajeContacto


class CitaForm(forms.ModelForm):
    fecha_hora = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'type': 'datetime-local', 'class': 'form-control'},
            format='%Y-%m-%dT%H:%M'
        ),
        input_formats=['%Y-%m-%dT%H:%M'],
        label='Fecha y hora deseada'
    )

    class Meta:
        model = CitaReserva
        fields = ['nombre_dueno', 'telefono', 'nombre_mascota', 'raza_mascota', 'servicio', 'fecha_hora', 'notas']
        widgets = {
            'nombre_dueno': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Tu nombre completo'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': '619 43 98 03'
            }),
            'nombre_mascota': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Nombre de tu peludo'
            }),
            'raza_mascota': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Raza (opcional)'
            }),
            'servicio': forms.Select(attrs={'class': 'form-control'}),
            'notas': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 3,
                'placeholder': 'Cuéntanos algo especial sobre tu mascota...'
            }),
        }


class ContactoForm(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'email', 'telefono', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Tu nombre'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 'placeholder': 'tu@email.com'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': '619 43 98 03'
            }),
            'mensaje': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 4,
                'placeholder': '¿En qué podemos ayudarte?'
            }),
        }
