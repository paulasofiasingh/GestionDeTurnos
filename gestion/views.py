from contextvars import Context
from pipes import Template
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from gestion.forms import TurnosForms
from gestion.models import Medico, Paciente
from django.contrib import messages
from .models import Turno
from django.db.models import Q
from .forms import SignUpForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    queryset = request.GET.get("buscar")
    if queryset:
        lista = Turno.objects.filter(
            Q(turno_id = queryset)
        )
    return render(request,'gestion/publica/index.html')

def create(request):
    if request.method == 'GET':
        turno_form_get = TurnosForms()
        return render(request, 'gestion/publica/form.html',{'turno_form':turno_form_get})
    else:
        try:
            print(request.FILES)
            turno_form = TurnosForms(request.POST, request.FILES)
            if(turno_form.is_valid()):
                messages.success(request,'El turno ha sido agendado exitosamente.')
                turno_form.save()
                return redirect('index')
            else :
                print("Ha ocurrido un error. Vuelva a intentarlo.")

        except ValueError:
            return render(request, 'form.html', {"turno_form": TurnosForms(), "error": "Error al crear el turno."})

def turnos(request):
    """turnos = Turno.objects.all()
    turnos = Turno.objects.values_list('id')"""
    turnos = list(Turno.objects.all())
    return render(request, 'gestion/publica/listar_turnos.html', {'turnos': turnos})

def detail(request, id):
    turno = get_object_or_404(Turno, pk=id)
    return render(request, 'gestion/publica/detail.html', {'turno':turno})

def buscar(request):
    queryset = request.GET.get("buscar")
    turno = get_object_or_404(Turno, pk=queryset)
    return render(request, 'gestion/publica/detail.html', {'turno':turno})

def update(request, id):
    return HttpResponse("Estás actualizando el turno %s." % id)

def signup(request):
    if request.method == 'GET':
        return render(request, 'gestion/publica/signup.html', {'userform': SignUpForm})
    else:
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
                return HttpResponse('Usuario creado satisfactoriamente')
            except ValueError:
                print(ValueError)
                return HttpResponse('El usuario ya existe')
        return HttpResponse('Las contraseñas no coinciden.')
