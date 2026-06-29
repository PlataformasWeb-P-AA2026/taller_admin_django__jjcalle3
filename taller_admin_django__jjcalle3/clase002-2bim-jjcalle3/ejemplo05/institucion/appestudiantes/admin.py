from django.contrib import admin

# Register your models here.
from appestudiantes.model import Estudiante, Ciclo

admin.site.register(Estudiante)
admin.site.register(Ciclo)
