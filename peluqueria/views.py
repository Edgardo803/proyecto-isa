"""Vistas para Coquettos Peluquería Canina."""

from django.shortcuts import render, redirect
from django.contrib import messages
from urllib.parse import quote
from .models import Servicio, ClientePeludo, Resena
from .forms import CitaForm, ContactoForm

# Número de WhatsApp de Isa (sin espacios, con prefijo España)
WHATSAPP_ISA = '34619439803'


def home(request):
    """Página principal con hero, servicios, galería y sección Kokillo."""
    servicios = Servicio.objects.all()[:4]
    clientes = ClientePeludo.objects.filter(es_estrella=True)[:5]
    resenas = Resena.objects.filter(visible=True)[:6]
    return render(request, 'peluqueria/home.html', {
        'servicios': servicios,
        'clientes': clientes,
        'resenas': resenas,
    })


def servicios(request):
    """Página completa de servicios."""
    todos_servicios = Servicio.objects.all()
    return render(request, 'peluqueria/servicios.html', {
        'servicios': todos_servicios,
    })


def galeria(request):
    """Galería de clientes peludos."""
    clientes = ClientePeludo.objects.all()
    return render(request, 'peluqueria/galeria.html', {
        'clientes': clientes,
    })


def cita(request):
    """Formulario de reserva de cita — guarda en BD y abre WhatsApp de Isa."""
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            cita_obj = form.save()

            # ── Construir mensaje de WhatsApp con todos los datos ──
            servicio_nombre = cita_obj.servicio.nombre if cita_obj.servicio else 'Sin especificar'
            fecha_str = cita_obj.fecha_hora.strftime('%d/%m/%Y a las %H:%M')
            raza_str = f' ({cita_obj.raza_mascota})' if cita_obj.raza_mascota else ''
            notas_str = f'\n📝 Notas: {cita_obj.notas}' if cita_obj.notas else ''

            mensaje = (
                f'🐾 *NUEVA SOLICITUD DE CITA — COQUETTOS*\n\n'
                f'👤 *Dueño/a:* {cita_obj.nombre_dueno}\n'
                f'📞 *Teléfono:* {cita_obj.telefono}\n'
                f'🐕 *Mascota:* {cita_obj.nombre_mascota}{raza_str}\n'
                f'✂️ *Servicio:* {servicio_nombre}\n'
                f'📅 *Fecha deseada:* {fecha_str}'
                f'{notas_str}\n\n'
                f'_Mensaje enviado desde la web de Coquettos_ 💕'
            )

            whatsapp_url = f'https://wa.me/{WHATSAPP_ISA}?text={quote(mensaje)}'

            # ── Guardar URL en sesión para el redirect ──
            request.session['whatsapp_url'] = whatsapp_url
            request.session['mascota_nombre'] = cita_obj.nombre_mascota

            return redirect('cita_confirmada')

        else:
            messages.error(request, '❌ Revisa el formulario, hay algún error.')
    else:
        form = CitaForm()
    return render(request, 'peluqueria/cita.html', {'form': form})


def cita_confirmada(request):
    """Página de confirmación que redirige a WhatsApp."""
    whatsapp_url = request.session.pop('whatsapp_url', None)
    mascota = request.session.pop('mascota_nombre', 'tu mascota')
    return render(request, 'peluqueria/cita_confirmada.html', {
        'whatsapp_url': whatsapp_url,
        'mascota': mascota,
    })


def contacto(request):
    """Página de contacto con formulario."""
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                '✅ ¡Mensaje recibido! Te responderemos lo antes posible. 💕'
            )
            return redirect('contacto')
        else:
            messages.error(request, '❌ Revisa el formulario, hay algún error.')
    else:
        form = ContactoForm()
    return render(request, 'peluqueria/contacto.html', {'form': form})
