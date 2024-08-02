from django.db import models


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    categoria_nombre = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoria'


class Noticia(models.Model):
    id_noticia = models.IntegerField(primary_key=True)
    titulo = models.CharField(unique=True, max_length=200)
    contenido = models.TextField()
    fecha_publica = models.DateTimeField()
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'noticia'