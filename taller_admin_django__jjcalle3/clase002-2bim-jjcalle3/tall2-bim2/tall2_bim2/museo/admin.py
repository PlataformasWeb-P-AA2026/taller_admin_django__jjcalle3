from django.contrib import admin
from .models import Museo, Guia, Exhibicion


@admin.register(Museo)
class MuseoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "ciudad", "anio_fund", "mostrar_costo", "mostrar_guia")

    def mostrar_costo(self, obj):
        return obj.costo_total_produccion()

    def mostrar_guia(self, obj):
        guia = obj.guia_mas_experiencia()
        if guia:
            return guia.nombre_completo
        return "-"