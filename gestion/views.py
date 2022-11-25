from contextvars import Context
from pipes import Template
from django.shortcuts import render
from django.http import HttpResponse
from gestion.forms import Turnos


# Create your views here.
def index(request):
    titulo = "Busca profesionales en tu ciudad"
    descripcion = "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Earum perspiciatis excepturi optio libero quasi beatae itaque, officiis numquam iste tempore dolor! Odio tempora sit rem tenetur consectetur eum atque iste?"
    especialidades =  [
            'Clínica médica',
            'Dermatología',
            'Gastroenterología'
            'Ginecología',
            'Nefrología',
            'Nutrición',
            'Traumatología'
            ]
    contexto = {
        "titulo": titulo, 
        "especialidades": especialidades,  
        "descripcion": descripcion,        
        }
    return render(request,'gestion/publica/index.html', contexto)

def create(request):
    if (request.method == 'POST'):
        turno_form = Turnos(request.POST)
        
    else:
        
        turno_form = Turnos()
    return render(request, 'gestion/publica/form.html',{'turno_form':turno_form})

def detail(request, id):
    return HttpResponse("Estás viendo el detalle del turno %s." % id)

def update(request, id):
    return HttpResponse("Estás actualizando el turno %s." % id)