from django.db import models
from apps.usuarios.models import Usuario
from apps.experimentos.models import Experimento

class Limpieza(models.Model):
    tarea = models.TextField()
    asignado_a = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': 'estudiante'})
    experimento = models.ForeignKey(Experimento, on_delete=models.CASCADE)
    completado = models.BooleanField(default=False)

    def __str__(self):
        return f"Tarea: {self.tarea} - Asignado a: {self.asignado_a.username}"
