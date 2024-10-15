from django.contrib import admin
from .models import Estado, Municipio, Localidad, Asentamiento

admin.site.register(Estado)
admin.site.register(Municipio)
admin.site.register(Localidad)
admin.site.register(Asentamiento)
