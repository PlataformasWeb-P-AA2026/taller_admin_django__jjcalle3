from django.db import models
import datetime as dt
# Create your models here.

class Estudiante(models.Model):
    opciones_tipo_estudiante = (

        ('becado', 'Estudiante Becado'),

        ('no-becado', 'Estudiante No Becado'),

        )

    nombre = models.CharField("Nombre de estudiante", max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    edad = models.IntegerField("edad de estudiante") # Verbose field names
    tipo_estudiante = models.CharField(max_length=30, \
            choices=opciones_tipo_estudiante)


    def __str__(self):
        return "%s - %s - %s - edad: %d - tipo: %s" % (self.nombre,
                self.apellido,
                self.cedula,
                self.edad,
                self.tipo_estudiante)

    def obtener_anio_nacimiento(self):
        """a"""
        return dt.datetime.now().year - self.edad
