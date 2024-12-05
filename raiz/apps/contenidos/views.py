from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Contenido

class ContenidoCreateView(CreateView):
    model = Contenido
    template_name = 'contenidos/contenido_form.html'
    fields = ['titulo', 'descripcion', 'recursos', 'creado_por']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = 'Crear'
        return context

class ContenidoListView(ListView):
    model = Contenido
    template_name = 'contenidos/contenido_lista.html'
    context_object_name = 'contenidos'

class ContenidoUpdateView(UpdateView):
    model = Contenido
    template_name = 'contenidos/contenido_form.html'
    fields = ['titulo', 'descripcion', 'recursos']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accion'] = 'Editar'
        return context

class ContenidoDeleteView(DeleteView):
    model = Contenido
    template_name = 'contenidos/contenido_confirmacion_eliminar.html'
    success_url = reverse_lazy('contenido-list')
