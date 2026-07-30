# 🐾 Coquettos Peluquería Canina

Sitio web oficial de **Coquettos Peluquería Canina** en Alhama de Murcia.
Desarrollado con **Django 6** · Python 3 · SQLite · CSS3 · JavaScript vanilla.

> "Más que belleza, creamos confianza" 💕

## ✨ Características

- Página principal con hero animado, servicios, galería y sección especial de **Kokillo** 🦸
- Galería de clientes con lightbox
- Formulario de reserva de citas → envío automático por **WhatsApp** a Isa
- Formulario de contacto
- Panel de administración Django para gestionar citas, reseñas y clientes
- Diseño responsive con animaciones CSS y JavaScript

## 🚀 Cómo ejecutar en local

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/proyecto-isa.git
cd proyecto-isa

# 2. Instalar dependencias
pip3 install django pillow --break-system-packages

# 3. Aplicar migraciones
python3 manage.py migrate

# 4. Cargar datos iniciales
python3 seed_data.py

# 5. Arrancar el servidor
python3 manage.py runserver
```

Abre el navegador en: **http://127.0.0.1:8000**

## 🔐 Panel Admin

- URL: `http://127.0.0.1:8000/admin`
- Usuario: `isa`
- Contraseña: `coquettos2024`

## 📁 Estructura del proyecto

```
proyecto-isa/
├── coquettos/          → Configuración Django (settings, urls)
├── peluqueria/         → App principal (models, views, templates, static)
├── media/              → Fotos y vídeos (Kokillo 🦸)
├── manage.py
├── seed_data.py        → Script para cargar datos iniciales
└── requirements.txt
```

## 📞 Contacto del negocio

- **Dirección**: C. Río Turia, 8, 30840 Alhama de Murcia
- **Teléfono**: 619 43 98 03
- **Google**: 4,9 ⭐ (26 reseñas)
