from django.urls import path
from .views import (
    ExperimentoListView,
    ExperimentoCreateView,
    ExperimentoDetailView,
    ExperimentoUpdateView,
    ExperimentoDeleteView,
)

urlpatterns = [
    path('', ExperimentoListView.as_view(), name='experimento-list'),
    path('crear/', ExperimentoCreateView.as_view(), name='experimento-create'),
    path('<int:pk>/', ExperimentoDetailView.as_view(), name='experimento-detail'),
    path('<int:pk>/editar/', ExperimentoUpdateView.as_view(), name='experimento-update'),
    path('<int:pk>/eliminar/', ExperimentoDeleteView.as_view(), name='experimento-delete'),
]
