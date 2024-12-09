from django.urls import path
from . import views

urlpatterns = [
    # Login y Logout
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),

    # Redirección por Rol
    path('panel/', views.redireccion_por_rol, name='panel'),

    # Paneles por Rol
    path('panel-estudiante/<str:etapa>/', views.PanelEstudianteView, name='panel-estudiante'),
    path('panel-profesor/', views.PanelProfesorView, name='panel-profesor'),
    path('panel-admin/', views.PanelAdminView, name='panel-admin'),

    # Gestión de Usuarios
    path('registrar-usuario/', views.registrar_usuario, name='registrar-usuario'),
]
