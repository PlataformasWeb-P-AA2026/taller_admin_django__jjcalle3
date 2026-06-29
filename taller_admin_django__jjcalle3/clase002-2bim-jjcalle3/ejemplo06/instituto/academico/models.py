from django.db import models

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % (self.nombre)


class Instructor(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return "%s" % (self.nombre)


class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    departamento = models.ForeignKey(
        Departamento,
        on_delete=models.CASCADE,
        related_name="cursos"
    )
    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.CASCADE,
        related_name="cursos"
    )

    def __str__(self):
        return "%s" % (self.titulo)


class Estudiante(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return "%s" % (self.nombre)


class Inscripcion(models.Model):
    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE,
        related_name="inscripciones"
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name="inscripciones"
    )
    fecha_inscripcion = models.DateTimeField()

    def __str__(self):
        return "%s %s" % (self.estudiante, self.curso)


class Tarea(models.Model):
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name="tareas"
    )
    titulo = models.CharField(max_length=200)
    fecha_entrega = models.DateTimeField()

    def __str__(self):
        return "%s" % (self.titulo)


class Entrega(models.Model):
    tarea = models.ForeignKey(
        Tarea,
        on_delete=models.CASCADE,
        related_name="entregas"
    )
    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE,
        related_name="entregas"
    )
    fecha_envio = models.DateTimeField()
    calificacion = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "%s %s %s" % (
            self.estudiante,
            self.tarea,
            self.calificacion
        )
