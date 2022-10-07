from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Bienvenidos")

def create(request):
    pass

def detail(request, id):
    return HttpResponse("Estás viendo el detalle del turno %s." % id)

def update(request, id):
    return HttpResponse("Estás actualizando el turno %s." % id)