from django.urls import path
from .views import (
    EvaluacionCreateView,
    EvaluacionListView,
    EvaluacionUpdateView,
    EvaluacionDeleteView,
    DiagnosticoSubmitView,
    BancoPreguntasView,
    eliminar_pregunta
)

urlpatterns = [
    # Gestión de Evaluaciones
    path('', EvaluacionListView.as_view(), name='evaluacion-list'),  # Ruta base para listar evaluaciones
    path('crear/', EvaluacionCreateView.as_view(), name='evaluacion-create'),
    path('editar/<int:pk>/', EvaluacionUpdateView.as_view(), name='evaluacion-update'),
    path('eliminar/<int:pk>/', EvaluacionDeleteView.as_view(), name='evaluacion-delete'),

    # Diagnóstico
    path('diagnostico/submit/<int:pk>/', DiagnosticoSubmitView, name='diagnostico-submit'),

    # Banco de Preguntas
    path('banco-preguntas/', BancoPreguntasView, name='banco-preguntas'),
    path('banco-preguntas/<int:experimento_id>/', BancoPreguntasView, name='banco-preguntas-experimento'),
    path('banco-preguntas/<str:tipo>/', BancoPreguntasView, name='banco-preguntas-tipo'),
    path('pregunta/eliminar/<int:pk>/', eliminar_pregunta, name='eliminar-pregunta'),  # Vista para eliminar preguntas
]
