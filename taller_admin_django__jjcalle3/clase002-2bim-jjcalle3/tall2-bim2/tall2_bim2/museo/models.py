from django.db import models

# Create your models here.
from django.db import models

class Museo(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    ciudad = models.CharField(max_length=30)
    anio_fund = models.IntegerField()

    def __str__(self):
        return "%s - %s - %d" % (
            self.nombre,
            self.ciudad,
            self.anio_fund
        )

    # Costo total de producción de todas las exhibiciones
    def costo_total_produccion(self):
        total = 0

        for guia in self.guias.all():
            for exhibicion in guia.exhibiciones.all():
                total += exhibicion.costo_produccion

        return total

    # Devuelve un solo guía con mayor experiencia
    def guia_mas_experiencia(self):
        mayor = None

        for guia in self.guias.all():
            if mayor is None or guia.anios_experiencia > mayor.anios_experiencia:
                mayor = guia

        return mayor

    # Por si hay más de un guía con la experiencia máxima
    def guias_mas_experimentados(self):
        mayor = 0

        for guia in self.guias.all():
            if guia.anios_experiencia > mayor:
                mayor = guia.anios_experiencia

        lista = []

        for guia in self.guias.all():
            if guia.anios_experiencia == mayor:
                lista.append(guia)

        return lista


class Guia(models.Model):
    nombre_completo = models.CharField(max_length=60)
    anios_experiencia = models.IntegerField()
    idiomas_hablados = models.CharField(max_length=30)

    museo = models.ForeignKey(
        Museo,
        on_delete=models.CASCADE,
        related_name="guias"
    )

    def __str__(self):
        return "%s - %d - %s" % (
            self.nombre_completo,
            self.anios_experiencia,
            self.idiomas_hablados
        )


class Exhibicion(models.Model):
    titulo_exhibicion = models.CharField(max_length=30)
    duracion_meses = models.IntegerField()
    costo_produccion = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    tematica = models.CharField(max_length=30)

    guia = models.ForeignKey(
        Guia,
        on_delete=models.CASCADE,
        related_name="exhibiciones"
    )

    def __str__(self):
        return "%s - %d - %.2f - %s" % (
            self.titulo_exhibicion,
            self.duracion_meses,
            self.costo_produccion,
            self.tematica
        )