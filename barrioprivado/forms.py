from django import forms
from .models import Residente, Sector

class formularioResidente(forms.Form):
    nombre = forms.CharField()
    edad = forms.CharField()
    direccion = forms.CharField()
    email = forms.EmailField()
    telefono = forms.IntegerField()
    GENERO_CHOICES = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('N', 'No binario'),
    ]
    genero = forms.ChoiceField(choices=[('F', 'Femenino'), ('M', 'Masculino'), ('N', 'No especificado')])
    dni = forms.IntegerField()
    

class formularioInvitado(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    telefono = forms.IntegerField()
    residente = forms.ModelChoiceField(queryset=Residente.objects.all())


    
class formularioStaff(forms.Form):
    nombre = forms.CharField()
    sector = forms.ModelChoiceField(queryset=Sector.objects.all())
    telefono = forms.IntegerField()
    
