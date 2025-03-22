# Create your models here.
from django.db import models
from django.utils.timezone import now


class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    fecha_registro = models.DateTimeField(default=now)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
