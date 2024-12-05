from django.urls import path
from .views import (
    LoginView,
    LogoutView,
    redireccion_por_rol,
    PanelEstudianteView,
    PanelProfesorView,
    PanelAdminView,
    registrar_usuario,
)

urlpatterns = [
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
    path('panel/', redireccion_por_rol, name='panel'),
    path('panel/estudiante/', PanelEstudianteView, name='panel-estudiante'),
    path('panel/profesor/', PanelProfesorView, name='panel-profesor'),
    path('panel/admin/', PanelAdminView, name='panel-admin'),
    path('panel/admin/registrar-usuario/', registrar_usuario, name='registrar-usuario'),
]
