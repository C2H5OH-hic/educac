from django.db import models
from apps.usuarios.models import Usuario

class Contenido(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    recursos = models.TextField()
    creado_por = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
