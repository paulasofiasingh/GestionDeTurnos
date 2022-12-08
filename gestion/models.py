from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Medico(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    apellido = models.CharField(max_length=50,verbose_name='Apellido')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    especialidad = models.CharField(max_length=150,verbose_name='Especialidad')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Paciente(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    apellido = models.CharField(max_length=50,verbose_name='Apellido')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    obra_social = models.CharField(max_length=150,verbose_name='Obra Social')
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Turno(models.Model):
    medico = models.ForeignKey(Medico,on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente,on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name='Fecha',null=False,default=None)
    observacion = models.CharField(max_length=150,verbose_name='Observacion')

    def __str__(self):
        return f"{self.id} {self.fecha} {self.medico}"
