from django import forms

class Turnos(forms.Form):
    fecha = forms.DateField(
        label='Fecha',
        widget=forms.SelectDateWidget)
    observaciones = forms.CharField(
        label='Observaciones',
        max_length=150,
        widget= forms.Textarea(attrs={'rows':5}))