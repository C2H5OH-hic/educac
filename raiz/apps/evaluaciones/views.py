from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Evaluacion

class EvaluacionCreateView(CreateView):
    model = Evaluacion
    template_name = 'evaluaciones/evaluacion_form.html'
    fields = ['tipo', 'puntaje', 'observaciones', 'experimento', 'estudiante']

class EvaluacionListView(ListView):
    model = Evaluacion
    template_name = 'evaluaciones/evaluacion_lista.html'
    context_object_name = 'evaluaciones'