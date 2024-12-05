from django.contrib import admin
from django.urls import path, include
from apps.usuarios.views import LoginView  # Importa la vista personalizada para login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView, name='home'),  # La página principal será el login
    path('usuarios/', include('apps.usuarios.urls')),  # Rutas de Usuarios
    path('contenidos/', include('apps.contenidos.urls')),  # Rutas de Contenidos
    path('experimentos/', include('apps.experimentos.urls')),  # Rutas de Experimentos
    path('evaluaciones/', include('apps.evaluaciones.urls')),  # Rutas de Evaluaciones
    path('limpieza/', include('apps.limpieza.urls')),  # Rutas de Limpieza
]