from django.db import models

# Create your models here.


class Profesion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Profesiones'
        ordering = ['id']
        # Modifica el Nombre de la Tabla en la Base de Datos
        # db_table = 'Persona'


class Distrito(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural: 'Distrito'


class Persona(models.Model):
    nombre = models.CharField(max_length = 50)
    apellidoPaterno = models.CharField(max_length=50)
    apellidoMaterno = models.CharField(max_length=50)
    celular = models.CharField(max_length=9)
    coordenadas = models.CharField(max_length=100, null=True)
    imagen = models.CharField(max_length=500, null=True)
    profesion = models.ForeignKey(Profesion, on_delete=models.CASCADE)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellidoPaterno)

    class Meta:
        verbose_name_plural: 'Personas'
