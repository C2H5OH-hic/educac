from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Limpieza

class LimpiezaCreateView(CreateView):
    model = Limpieza
    template_name = 'limpieza/limpieza_form.html'
    fields = ['tarea', 'asignado_a', 'experimento']

class LimpiezaListView(ListView):
    model = Limpieza
    template_name = 'limpieza/limpieza_lista.html'
    context_object_name = 'tareas'