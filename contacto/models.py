from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15, blank=True, null=True)
    asunto = models.CharField(max_length=200)
    mensaje = models.TextField()
    contacto = models.CharField(max_length=10, choices=[('email', 'Correo electrónico'), ('telefono', 'Teléfono')])

    def __str__(self):
        return f'{self.nombre} - {self.asunto}'
