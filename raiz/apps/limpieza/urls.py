from django.urls import path
from .views import LimpiezaCreateView, LimpiezaListView

urlpatterns = [
    path('', LimpiezaListView.as_view(), name='limpieza-list'),
    path('crear/', LimpiezaCreateView.as_view(), name='limpieza-create'),
]
