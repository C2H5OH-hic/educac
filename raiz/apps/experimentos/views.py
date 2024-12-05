from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Experimento

class ExperimentoListView(LoginRequiredMixin, ListView):
    """
    Vista para listar los experimentos según el rol del usuario.
    """
    model = Experimento
    template_name = 'experimentos/experimento_lista.html'
    context_object_name = 'experimentos'

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Experimento.objects.all()  # Todos los experimentos para el superusuario
        elif user.rol == 'profesor':
            return Experimento.objects.filter(profesor=user)  # Solo los experimentos creados por el profesor
        elif user.rol == 'estudiante':
            return Experimento.objects.filter(estudiantes=user)  # Experimentos asignados al estudiante
        return Experimento.objects.none()

class ExperimentoCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    Vista para crear experimentos. Solo accesible para profesores.
    """
    model = Experimento
    template_name = 'experimentos/experimento_form.html'
    fields = ['nombre', 'descripcion', 'materiales', 'procedimiento', 'fecha', 'contenido']

    def test_func(self):
        return self.request.user.rol == 'profesor'

    def form_valid(self, form):
        form.instance.profesor = self.request.user  # Asigna automáticamente al profesor creador
        return super().form_valid(form)

class ExperimentoDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """
    Vista para mostrar los detalles de un experimento.
    Acceso permitido solo al profesor creador o a los estudiantes asignados.
    """
    model = Experimento
    template_name = 'experimentos/experimento_detalle.html'
    context_object_name = 'experimento'

    def test_func(self):
        experimento = self.get_object()
        user = self.request.user
        return experimento.profesor == user or user in experimento.asignado_a.all()
