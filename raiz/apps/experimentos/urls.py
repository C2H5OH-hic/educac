from django.urls import path
from .views import ExperimentoListView, ExperimentoCreateView, ExperimentoDetailView

urlpatterns = [
    path('', ExperimentoListView.as_view(), name='experimento-list'),
    path('crear/', ExperimentoCreateView.as_view(), name='experimento-create'),
    path('<int:pk>/', ExperimentoDetailView.as_view(), name='experimento-detail'),
]