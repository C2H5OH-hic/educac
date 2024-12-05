from django.db import models
from apps.usuarios.models import Usuario
from apps.experimentos.models import Experimento

class Evaluacion(models.Model):
    TIPOS = [
        ('previa', 'Previa'),
        ('final', 'Final'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPOS)
    puntaje = models.IntegerField()
    observaciones = models.TextField()
    experimento = models.ForeignKey(Experimento, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': 'estudiante'})

    def __str__(self):
        return f"Evaluación {self.get_tipo_display()} - {self.experimento.nombre} ({self.estudiante.username})"
