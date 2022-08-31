from __future__ import unicode_literals
from distutils.command.upload import upload

from django.db import models

from ..adopcion.models import Persona

# Create your models here.

# Modelo avacuna para la base de datos
class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return '{}'.format(self.nombre)

# Modelo Mascota para la base de datos
class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacuna)
    foto = models.ImageField(upload_to="images/", null=True, blank=True)

    