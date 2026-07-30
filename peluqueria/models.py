"""Modelos de datos para Coquettos Peluquería Canina."""

from django.db import models


class Servicio(models.Model):
    ICONO_CHOICES = [
        ('✂️', 'Tijeras'),
        ('🛁', 'Bañera'),
        ('💅', 'Manicura'),
        ('💆', 'Spa'),
        ('🎀', 'Accesorios'),
        ('🐾', 'Pata'),
    ]
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    icono = models.CharField(max_length=10, choices=ICONO_CHOICES, default='🐾')
    precio_desde = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    destacado = models.BooleanField(default=False)
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['orden']
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return self.nombre


class ClientePeludo(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100, blank=True)
    descripcion = models.TextField(blank=True)
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)
    es_estrella = models.BooleanField(default=False, help_text='Mostrar en portada')
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['orden']
        verbose_name = 'Cliente Peludo'
        verbose_name_plural = 'Clientes Peludos'

    def __str__(self):
        return self.nombre


class Resena(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    texto = models.TextField()
    puntuacion = models.PositiveSmallIntegerField(choices=[(i, f'{i} estrellas') for i in range(1, 6)], default=5)
    fecha = models.DateField(auto_now_add=True)
    visible = models.BooleanField(default=True)

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Reseña'
        verbose_name_plural = 'Reseñas'

    def __str__(self):
        return f'{self.nombre_cliente} — {self.puntuacion}⭐'

    def estrellas_lista(self):
        return range(self.puntuacion)

    def estrellas_vacias(self):
        return range(5 - self.puntuacion)


class CitaReserva(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]
    nombre_dueno = models.CharField(max_length=100, verbose_name='Nombre del dueño')
    telefono = models.CharField(max_length=20, verbose_name='Teléfono')
    nombre_mascota = models.CharField(max_length=100, verbose_name='Nombre de la mascota')
    raza_mascota = models.CharField(max_length=100, blank=True, verbose_name='Raza (opcional)')
    servicio = models.ForeignKey(Servicio, on_delete=models.SET_NULL, null=True, verbose_name='Servicio')
    fecha_hora = models.DateTimeField(verbose_name='Fecha y hora deseada')
    notas = models.TextField(blank=True, verbose_name='Notas adicionales')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    creada_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['fecha_hora']
        verbose_name = 'Reserva de Cita'
        verbose_name_plural = 'Reservas de Citas'

    def __str__(self):
        return f'{self.nombre_mascota} ({self.nombre_dueno}) — {self.fecha_hora.strftime("%d/%m/%Y %H:%M")}'


class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    mensaje = models.TextField()
    leido = models.BooleanField(default=False)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creado_en']
        verbose_name = 'Mensaje de Contacto'
        verbose_name_plural = 'Mensajes de Contacto'

    def __str__(self):
        return f'{self.nombre} — {self.creado_en.strftime("%d/%m/%Y")}'
