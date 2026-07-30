"""Script para poblar la base de datos con datos iniciales de Coquettos."""

import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coquettos.settings')
sys.path.insert(0, '/Users/USUARIO/Desktop/proyecto-isa')
django.setup()

from django.contrib.auth.models import User
from peluqueria.models import Servicio, ClientePeludo, Resena

# ── Superusuario ──
if not User.objects.filter(username='isa').exists():
    User.objects.create_superuser('isa', 'isa@coquettos.es', 'coquettos2024')
    print("✅ Superusuario 'isa' creado (contraseña: coquettos2024)")
else:
    print("ℹ️  Superusuario 'isa' ya existe")

# ── Servicios ──
servicios_data = [
    ('✂️', 'Corte y Peinado', 'Ya sea un corte de raza estándar o algo más personalizado, nuestro equipo está capacitado para hacerlo. Técnicas de última generación para un aspecto impecable.', None, True, 1),
    ('🛁', 'Baño y Aseo Premium', 'Mantén a tu mascota limpia y brillante. Productos de alta calidad que cuidan la piel y el pelaje, dejándola con un aspecto saludable y brillante.', None, True, 2),
    ('💅', 'Corte de Uñas', 'El cuidado adecuado de las uñas es esencial para la salud de tu mascota. Lo hacemos de forma segura y sin causar molestias.', None, False, 3),
    ('💆', 'Tratamientos de Spa', 'Desde baños de hidromasaje hasta masajes relajantes. Tu peludo se sentirá mimado, relajado y feliz.', None, True, 4),
    ('🎀', 'Accesorios y Perfumes', 'Lazos, pañuelos, perfumes exclusivos. Dale a tu mascota ese toque especial que la hará destacar y oler de maravilla.', None, False, 5),
    ('🐾', 'Pack Completo VIP', 'Baño + secado + corte + uñas + limpieza de oídos + perfume. El tratamiento más completo para una mascota impecable.', None, True, 6),
]

Servicio.objects.all().delete()
for icono, nombre, desc, precio, dest, orden in servicios_data:
    Servicio.objects.create(
        icono=icono, nombre=nombre, descripcion=desc,
        precio_desde=precio, destacado=dest, orden=orden
    )
print(f"✅ {len(servicios_data)} servicios creados")

# ── Clientes Peludos ──
clientes_data = [
    ('Briana', 'Pomerania', 'La más coqueta. Siempre lista para el postureo.', 'fotos/briana.jpg', True, 1),
    ('Doker', 'Bichón', 'Pequeño pero con mucho carácter. Le encanta el spa.', 'fotos/doker.jpg', True, 2),
    ('Odín', 'Pomerania Blanco', 'Esponjoso como una nube y tan adorable como parece.', 'fotos/odin.jpg', True, 3),
    ('Snausser', 'Schnauzer Gigante', 'El más serio de la pandilla, pero por dentro es un bebé.', 'fotos/snausser.jpg', True, 4),
    ('Tobi', 'Yorkshire Terrier', '¡Siempre con la lengua fuera de alegría! El alma de la fiesta.', 'fotos/tobi.jpg', True, 5),
]

ClientePeludo.objects.all().delete()
for nombre, raza, desc, foto, estrella, orden in clientes_data:
    ClientePeludo.objects.create(
        nombre=nombre, raza=raza, descripcion=desc,
        foto=foto, es_estrella=estrella, orden=orden
    )
print(f"✅ {len(clientes_data)} clientes peludos creados")

# ── Reseñas ──
resenas_data = [
    ('María García', '¡Increíble! Mi Briana sale siempre preciosa de Coquettos. Isa tiene unas manos mágicas y un trato excepcional. ¡100% recomendable!', 5),
    ('Carlos Martínez', 'Llevamos a Kokillo desde hace años y siempre sale contentísimo. El trato es maravilloso, casi como familia. ¡Coquettos es lo mejor de Alhama!', 5),
    ('Ana Sánchez', 'El mejor sitio para tu peludo sin duda. Isa se preocupa de verdad por los animales. Odín sale siempre como un rey. ¡Gracias Coquettos!', 5),
    ('José Fernández', 'Snausser es muy nervioso pero con Isa está tranquilísimo. Tiene un don especial con los animales. El corte siempre perfecto. ¡Lo recomiendo!', 5),
    ('Laura Romero', 'Tobi salió como nuevo. Muy limpio, bien recortado y oliendo fenomenal. Isa es una profesional de verdad. Repetiremos seguro!', 5),
    ('Pedro Molina', 'Servicio impecable desde el primer día. Isa cuida a nuestros perros como si fueran suyos. El precio muy razonable para la calidad que ofrecen.', 5),
]

Resena.objects.all().delete()
for nombre, texto, punt in resenas_data:
    Resena.objects.create(nombre_cliente=nombre, texto=texto, puntuacion=punt, visible=True)
print(f"✅ {len(resenas_data)} reseñas creadas")

print("\n🐾 ¡Base de datos lista! Coquettos está listo para brillar.")
print("🔗 Admin: http://127.0.0.1:8000/admin  →  usuario: isa  /  contraseña: coquettos2024")
