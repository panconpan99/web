from django.contrib import admin
from .models import Representante,Cotizacion,Servicio,Empresa

# Register your models here.

admin.site.register(Representante)
admin.site.register(Cotizacion)
admin.site.register(Servicio)
admin.site.register(Empresa)