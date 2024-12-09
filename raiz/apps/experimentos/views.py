from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Experimento
from .forms import ExperimentoForm


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
            return Experimento.objects.filter(profesor=user)  # Experimentos creados por el profesor
        elif user.rol == 'estudiante':
            return Experimento.objects.filter(asignado_a=user)  # Experimentos asignados al estudiante
        return Experimento.objects.none()


class ExperimentoCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    Vista para crear un nuevo experimento, solo para profesores.
    """
    model = Experimento
    form_class = ExperimentoForm
    template_name = 'experimentos/experimento_form.html'
    success_url = reverse_lazy('experimento-list')

    def test_func(self):
        return self.request.user.rol == 'profesor'

    def form_valid(self, form):
        form.instance.profesor = self.request.user
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


class ExperimentoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Vista para editar un experimento, solo para el profesor creador.
    """
    model = Experimento
    form_class = ExperimentoForm
    template_name = 'experimentos/experimento_form.html'
    success_url = reverse_lazy('experimento-list')

    def test_func(self):
        experimento = self.get_object()
        return self.request.user == experimento.profesor


class ExperimentoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Vista para eliminar un experimento, solo para el profesor creador.
    """
    model = Experimento
    template_name = 'experimentos/experimento_confirmar_eliminacion.html'
    success_url = reverse_lazy('experimento-list')

    def test_func(self):
        experimento = self.get_object()
        return self.request.user == experimento.profesor
