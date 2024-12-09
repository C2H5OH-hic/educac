from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Evaluacion, Pregunta
from .forms import PreguntaForm
from apps.experimentos.models import Experimento

class EvaluacionCreateView(CreateView):
    model = Evaluacion
    template_name = 'evaluaciones/evaluacion_form.html'
    fields = ['tipo', 'puntaje', 'observaciones', 'experimento', 'estudiante']
    success_url = reverse_lazy('evaluacion-list')

class EvaluacionListView(ListView):
    model = Evaluacion
    template_name = 'evaluaciones/evaluacion_lista.html'
    context_object_name = 'evaluaciones'

@login_required
def DiagnosticoSubmitView(request, pk):
    """
    Maneja el envío de respuestas de la evaluación diagnóstica.
    """
    if request.method == 'POST':
        # Obtener el experimento relacionado
        experimento = get_object_or_404(Experimento, pk=pk)

        # Obtener la evaluación diagnóstica asociada al estudiante y experimento
        evaluacion = Evaluacion.objects.filter(
            tipo='previa', 
            estudiante=request.user,
            experimento=experimento
        ).first()

        if evaluacion:
            # Procesar respuestas del formulario
            for key, value in request.POST.items():
                if key.startswith('pregunta'):
                    print(f"Respuesta a {key}: {value}")  # Aquí puedes almacenar las respuestas si es necesario

            # Redirigir a la etapa del experimento
            return redirect('panel-estudiante', etapa='experimento')

    # Si no es un POST o no hay evaluación, redirigir al diagnóstico
    return redirect('panel-estudiante', etapa='diagnostico')

@login_required
def BancoPreguntasView(request, experimento_id=None, tipo=None):
    """
    Gestiona el banco de preguntas, permitiendo filtrar por tipo y experimento.
    """
    if request.user.rol != 'profesor':
        return redirect('panel')

    # Obtener todas las preguntas inicialmente
    preguntas = Pregunta.objects.all()

    # Filtrar por experimento si se proporciona
    if experimento_id:
        preguntas = preguntas.filter(experimento_id=experimento_id)

    # Filtrar por tipo si se proporciona
    if tipo:
        preguntas = preguntas.filter(tipo=tipo)

    # Manejo del formulario para agregar nuevas preguntas
    if request.method == 'POST':
        form = PreguntaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('banco-preguntas')  # Redirigir al banco general
    else:
        form = PreguntaForm()

    return render(request, 'evaluaciones/banco_preguntas.html', {
        'preguntas': preguntas,
        'form': form,
    })

@login_required
def eliminar_pregunta(request, pk):
    pregunta = get_object_or_404(Pregunta, pk=pk)

    if request.user.rol == 'profesor':
        pregunta.delete()

    return redirect('banco-preguntas')

class EvaluacionUpdateView(UpdateView):
    """
    Vista para actualizar una evaluación existente.
    """
    model = Evaluacion
    template_name = 'evaluaciones/evaluacion_form.html'
    fields = ['tipo', 'puntaje', 'observaciones', 'experimento', 'estudiante']
    success_url = reverse_lazy('evaluacion-list')

class EvaluacionDeleteView(DeleteView):
    """
    Vista para eliminar una evaluación.
    """
    model = Evaluacion
    template_name = 'evaluaciones/evaluacion_confirmar_eliminacion.html'
    success_url = reverse_lazy('evaluacion-list')