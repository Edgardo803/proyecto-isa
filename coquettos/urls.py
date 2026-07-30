"""URL configuration for Coquettos project."""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = '🐾 Coquettos Admin'
admin.site.site_title = 'Coquettos Peluquería Canina'
admin.site.index_title = 'Panel de Administración'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('peluqueria.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
