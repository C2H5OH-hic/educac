from django.db import models
from apps.usuarios.models import Usuario

class Horario(models.Model):
    dia = models.CharField(
        max_length=10,
        choices=[
            ('Lunes', 'Lunes'),
            ('Martes', 'Martes'),
            ('Miércoles', 'Miércoles'),
            ('Jueves', 'Jueves'),
            ('Viernes', 'Viernes'),
        ]
    )
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    profesor = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        limit_choices_to={'rol': 'profesor'},
        related_name='horarios_como_profesor'
    )
    estudiante = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        limit_choices_to={'rol': 'estudiante'},
        related_name='horarios_como_estudiante'
    )
    experimento = models.ForeignKey(
        'experimentos.Experimento',
        on_delete=models.CASCADE,
        related_name='horarios_relacionados'  # Nombre único para evitar conflictos
    )

    def __str__(self):
        return f"{self.dia} {self.hora_inicio}-{self.hora_fin}: {self.profesor.username} - {self.estudiante.username} - {self.experimento.nombre}"
