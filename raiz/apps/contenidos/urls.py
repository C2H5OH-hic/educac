from django.urls import path
from .views import ContenidoCreateView, ContenidoListView, ContenidoUpdateView, ContenidoDeleteView

urlpatterns = [
    path('', ContenidoListView.as_view(), name='contenido-list'),
    path('crear/', ContenidoCreateView.as_view(), name='contenido-create'),
    path('<int:pk>/editar/', ContenidoUpdateView.as_view(), name='contenido-update'),
    path('<int:pk>/eliminar/', ContenidoDeleteView.as_view(), name='contenido-delete'),
]


from django.urls import path
from .views import ContenidoCreateView, ContenidoListView, ContenidoUpdateView, ContenidoDeleteView

urlpatterns = [
    path('', ContenidoListView.as_view(), name='contenido-list'),
    path('crear/', ContenidoCreateView.as_view(), name='contenido-create'),
    path('<int:pk>/editar/', ContenidoUpdateView.as_view(), name='contenido-update'),
    path('<int:pk>/eliminar/', ContenidoDeleteView.as_view(), name='contenido-delete'),
]
