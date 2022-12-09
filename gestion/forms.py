from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.forms import ModelForm, ValidationError
from .models import Paciente, Turno, Medico

username_validator = UnicodeUsernameValidator()

def solo_caracteres(value):
    if any(char.isdigit() for char in value ):
        raise ValidationError('El nombre no puede contener números. %(valor)s',
                            params={'valor':value})

class RegistrarUsuarioForm(UserCreationForm):
    obra_social = forms.CharField(max_length=150)
    nombre = forms.CharField(max_length=50, validators=[solo_caracteres])
    apellido = forms.CharField(max_length=50, validators=[solo_caracteres])
    fecha_nacimiento = forms.DateField(
        label='Fecha de nacimiento', 
        widget=forms.DateInput(attrs={'class':'form-control md-5','type':'date'}))
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'obra_social', 'nombre', 'apellido', 'fecha_nacimiento']

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
        ##queryset=Paciente.objects.filter(usuario=15),
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