from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioAdminForm
from apps.experimentos.models import Experimento 

# Login
def LoginView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('panel')
        else:
            return render(request, 'usuarios/login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'usuarios/login.html')

# Logout
def LogoutView(request):
    logout(request)
    return redirect('login')

# Redirección por Rol
@login_required
def redireccion_por_rol(request):
    # Redirigir superusuarios al panel-admin
    if request.user.is_superuser:
        return redirect('panel-admin')

    # Redirigir según rol
    if request.user.rol == 'estudiante':
        return redirect('panel-estudiante')
    elif request.user.rol == 'profesor':
        return redirect('panel-profesor')

    # Redirigir al login si no se cumple ninguna condición
    return redirect('login')

# Panel del Estudiante
@login_required
def PanelEstudianteView(request):
    if request.user.rol != 'estudiante':
        return redirect('panel')  # Redirige a otro panel si no es estudiante

    # Obtiene los experimentos asignados al estudiante
    experimentos = Experimento.objects.filter(asignado_a=request.user)
    return render(request, 'usuarios/panel_estudiante.html', {'experimentos': experimentos})

# Panel del Profesor
@login_required
def PanelProfesorView(request):
    if request.user.rol != 'profesor':
        return redirect('panel')
    return render(request, 'usuarios/panel_profesor.html')

# Panel del Admin
@login_required
def PanelAdminView(request):
    if not request.user.is_superuser:
        return redirect('panel')
    return render(request, 'usuarios/panel_admin.html')

@login_required
def PanelEstudianteView(request):
    if request.user.rol != 'estudiante':
        return redirect('panel')  # Redirige si no es estudiante

    # Obtén los experimentos asignados al estudiante
    experimentos = Experimento.objects.filter(asignado_a=request.user)
    return render(request, 'usuarios/panel_estudiante.html', {'experimentos': experimentos})

@login_required
def registrar_usuario(request):
    if not request.user.is_superuser:
        return redirect('panel')

    if request.method == 'POST':
        form = RegistroUsuarioAdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('panel-admin')
    else:
        form = RegistroUsuarioAdminForm()

    return render(request, 'usuarios/registrar_usuario.html', {'form': form})