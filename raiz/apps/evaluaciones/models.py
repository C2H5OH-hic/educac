from django.db import models
from apps.usuarios.models import Usuario
from apps.experimentos.models import Experimento

class Pregunta(models.Model):
    TIPOS = [
        ('diagnostica', 'Diagnóstica'),
        ('final', 'Final'),
    ]
    texto = models.TextField()
    experimento = models.ForeignKey(Experimento, on_delete=models.CASCADE, related_name='preguntas')
    tipo = models.CharField(max_length=15, choices=TIPOS)  # Reagregado

    def __str__(self):
        return f"{self.get_tipo_display()}: {self.texto[:50]} (Experimento: {self.experimento.nombre})"

class Evaluacion(models.Model):
    TIPOS = [
        ('previa', 'Diagnóstica'),
        ('final', 'Final'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPOS)
    puntaje = models.IntegerField(blank=True, null=True)  # Ahora opcional
    observaciones = models.TextField(blank=True, null=True)  # Opcional para comentarios
    experimento = models.ForeignKey(Experimento, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': 'estudiante'})
    preguntas = models.ManyToManyField(Pregunta, related_name='evaluaciones')  # Relación directa con preguntas

    def __str__(self):
        return f"Evaluación {self.get_tipo_display()} - {self.experimento.nombre} ({self.estudiante.username})"
