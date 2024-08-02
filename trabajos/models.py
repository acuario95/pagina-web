from django.db import models

# Create your models here.

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    liga = models.CharField(max_length=200)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='imgTrabajo')
