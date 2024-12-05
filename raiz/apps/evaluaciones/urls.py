from django.urls import path
from .views import EvaluacionCreateView, EvaluacionListView

urlpatterns = [
    path('', EvaluacionListView.as_view(), name='evaluacion-list'),
    path('crear/', EvaluacionCreateView.as_view(), name='evaluacion-create'),
]
