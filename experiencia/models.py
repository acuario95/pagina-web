
from django.db import models

class Experiencia(models.Model):
    puesto = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='experiencias/', null=True, blank=True)

    def __str__(self):
        return f"{self.empresa}"
