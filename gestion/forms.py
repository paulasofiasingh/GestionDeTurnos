from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.forms import ModelForm
from .models import Paciente, Turno, Medico

username_validator = UnicodeUsernameValidator()

class SignUpForm(UserCreationForm):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    fecha_nacimiento = forms.DateField(
        label='Fecha de nacimiento', 
        widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    obra_social = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('nombre', 'apellido', 'fecha_nacimiento', 'obra_social', 'username')

class TurnosForms(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ['medico', 'paciente', 'fecha', 'observacion']
    
    medico = forms.ModelChoiceField(
        queryset=Medico.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    paciente = forms.ModelChoiceField(
        queryset=Paciente.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    fecha = forms.DateField(
            label='Fecha', 
            widget=forms.DateInput(attrs={'class':'form-control','type':'date'})
        )
    observacion = forms.CharField(
        label='Observaciones',
        max_length=150,
        widget= forms.Textarea(attrs={'rows':5, 'class':'form-control'}))

"""
class PacienteForm(forms.ModelForm):
     class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'obra_social']

        nombre = forms.CharField(
            max_length=50,
            label='Nombre'
        )
        apellido = forms.CharField(
            max_length=50,
            label='Apellido'
        )
        fecha_nacimiento = forms.DateField(
            label='Fecha de nacimiento', 
            widget=forms.DateInput(attrs={'class':'form-control','type':'date'})
        )
        obra_social = forms.CharField(
            max_length=150,
            label='Obra social'
        )
"""


