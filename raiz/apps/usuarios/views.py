from datetime import datetime
import locale
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from apps.horarios.models import Horario
from apps.evaluaciones.models import Evaluacion
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
    if request.user.is_superuser:
        return redirect('panel-admin')
    elif request.user.rol == 'estudiante':
        return redirect('panel-estudiante', etapa='diagnostico')
    elif request.user.rol == 'profesor':
        return redirect('panel-profesor')
    else:
        return render(request, 'usuarios/error.html', {'error': 'Rol desconocido'})

# Panel del Estudiante con manejo de etapas
@login_required
def PanelEstudianteView(request, etapa):
    if request.user.rol != 'estudiante':
        return redirect('panel')

    # Obtén la fecha y hora actuales
    now = datetime.now()
    dia_actual = now.strftime('%A')  # Ejemplo: 'Monday'
    hora_actual = now.time()

    # Mapeo de días en inglés a español
    dias_ingles_a_espanol = {
        'Monday': 'Lunes',
        'Tuesday': 'Martes',
        'Wednesday': 'Miércoles',
        'Thursday': 'Jueves',
        'Friday': 'Viernes',
        'Saturday': 'Sábado',
        'Sunday': 'Domingo',
    }
    dia_actual = dias_ingles_a_espanol.get(dia_actual, dia_actual)

    # Log para depuración
    print(f"Usuario: {request.user.username}, Día: {dia_actual}, Hora: {hora_actual}")

    # Filtrar horario actual
    horario_actual = Horario.objects.filter(
        estudiante=request.user,
        dia=dia_actual,
        hora_inicio__lte=hora_actual,
        hora_fin__gte=hora_actual
    ).first()

    if not horario_actual:
        return render(request, 'usuarios/panel_estudiante.html', {
            'mensaje': f"No tienes clases asignadas en este horario. (Día: {dia_actual}, Hora: {hora_actual})",
            'etapa': etapa,
        })

    # Obtener el experimento asignado al horario
    experimento = horario_actual.experimento

    # Buscar evaluación diagnóstica
    evaluacion_diagnostica = Evaluacion.objects.filter(
        tipo='previa',
        estudiante=request.user,
        experimento=experimento
    ).first()

    # Obtener preguntas de la evaluación diagnóstica
    preguntas = evaluacion_diagnostica.preguntas.all() if evaluacion_diagnostica else None

    # Log para depuración
    print(f"Horario Actual: {horario_actual}")
    print(f"Experimento Asignado: {experimento}")
    print(f"Evaluación Diagnóstica: {evaluacion_diagnostica}")
    print(f"Preguntas Diagnósticas: {preguntas}")

    return render(request, 'usuarios/panel_estudiante.html', {
        'etapa': etapa,
        'horario_actual': horario_actual,
        'experimento': experimento,
        'evaluacion_diagnostica': evaluacion_diagnostica,
        'preguntas': preguntas,
    })


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

# Registrar Usuario
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