from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Program(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='program_images/')
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return self.name
