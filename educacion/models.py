from django.db import models

class Education(models.Model):
    estudios = models.CharField(max_length=100)
    institucion = models.CharField(max_length=255)
    lugar = models.CharField(max_length=255)

    def __str__(self):
        return self.estudios
