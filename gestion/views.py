from django.shortcuts import render, redirect, get_object_or_404
from gestion.forms import TurnosForms
from gestion.models import Paciente
from django.contrib import messages
from .models import Turno
from django.db.models import Q
from .forms import RegistrarUsuarioForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    queryset = request.GET.get("buscar")
    if queryset:
        lista = Turno.objects.filter(
            Q(turno_id=queryset)
        )
    return render(request, 'gestion/publica/index.html')


def turnos(request):
    """turnos = Turno.objects.all()
    turnos = Turno.objects.values_list('id')"""
    turnos = list(Turno.objects.all())
    return render(request, 'gestion/publica/listar_turnos.html', {'turnos': turnos})


def detail(request, id):
    turno = get_object_or_404(Turno, pk=id)
    return render(request, 'gestion/publica/detail.html', {'turno': turno})


def buscar(request):
    queryset = request.GET.get("buscar")
    turno = get_object_or_404(Turno, pk=queryset)
    return render(request, 'gestion/publica/detail.html', {'turno': turno})


def signup(request):
    if request.method == 'GET':
        return render(request, 'gestion/publica/signup.html', {'userform': RegistrarUsuarioForm()})
    else:
        signUpForm = RegistrarUsuarioForm(request.POST, request.FILES)
        if(signUpForm.is_valid()):
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.create_user(
                        username=request.POST['username'],
                        password=request.POST['password1'])
                    user.save()
                    paciente = Paciente.objects.create(
                        nombre=request.POST['nombre'],
                        apellido=request.POST['apellido'],
                        fecha_nacimiento=request.POST['fecha_nacimiento'],
                        obra_social=request.POST['obra_social'],
                        usuario_id=user.pk)
                    paciente.save()
                    login(request, user)
                    return redirect('/sesion/')
                except IntegrityError:
                    return render(request, 'gestion/publica/signup.html', {
                        'userform': RegistrarUsuarioForm(),
                        "error": 'El usuario ya existe'
                    })
        return render(request, 'gestion/publica/signup.html', {
            'userform': RegistrarUsuarioForm(),
            "error": signUpForm.errors
        })

@login_required(login_url='/login/')
def sesion(request):
    return render(request, 'gestion/publica/sesion.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('index')


def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'gestion/publica/iniciar_sesion.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'gestion/publica/iniciar_sesion.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o la contraseña es incorrecto.'
            })
        else:
            login(request, user)
            return redirect('sesion')

@login_required(login_url='/login/')

def create(request):
    paciente = Paciente.objects.filter(usuario = request.user)
    if request.method == 'GET':
        turno_form = TurnosForms()
        turno_form.fields['paciente'].queryset = paciente
        ##paciente_id = Paciente.objects.get(usuario = request.user).pk
        return render(request, 'gestion/publica/form.html', {'turno_form': turno_form})
    else:
        try:
            turno_form = TurnosForms(request.POST, request.FILES)
            turno_form.paciente = Paciente.objects.get(usuario = request.user).pk
            if (turno_form.is_valid()):
                data = turno_form.save()
                idturno = data.pk
                messages.success(
                    request, 'El turno ha sido agendado exitosamente. Id de turno: %s' %idturno)
                turno_form = TurnosForms()
                turno_form.fields['paciente'].queryset = paciente
                return render(request,'gestion/publica/form.html', {'turno_form':turno_form})
            else:
                messages.error(
                    request, 'No se ha podido asignar el turno. Revise los errores y vuelva a intentarlo.')
                return render(request,'gestion/publica/form.html', {'turno_form':turno_form})
        except ValueError:
            turno_form = TurnosForms()
            turno_form.fields['paciente'].queryset = paciente
            return render(request, 'gestion/publica/form.html', {"turno_form": turno_form, "error": "Error al crear el turno."})

@login_required(login_url='/login/')

def mis_turnos(request):
    pacienteid = Paciente.objects.get(usuario = request.user).pk
    turnos = Turno.objects.filter(paciente = pacienteid)
    return render(request, 'gestion/publica/mis_turnos.html', {'turnos': turnos})