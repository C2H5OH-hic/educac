from django.db import models
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class Experimento(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    materiales = models.TextField(blank=True, null=True)  # Lista separada por líneas
    procedimiento = models.TextField()
    fecha = models.DateField()
    contenido = models.TextField(blank=True, null=True)
    profesor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="experimentos_creados")
    asignado_a = models.ManyToManyField(Usuario, related_name="experimentos_asignados")

    def __str__(self):
        return self.nombre
