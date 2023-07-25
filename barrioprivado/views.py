from django.shortcuts import render, redirect
from .forms import formularioResidente, formularioInvitado, formularioStaff
from .models import Residente, Sector, Staff, Invitado
from django.contrib import messages



def form_residentes(request):
    if request.method == 'POST':
        formulario = formularioResidente(request.POST)
        
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            
            residente = Residente(nombre=informacion['nombre'],
                                 edad=informacion['edad'], 
                                 direccion=informacion['direccion'], 
                                 email=informacion['email'], 
                                 telefono=informacion['telefono'], 
                                 dni=informacion['dni'],
                                 genero=informacion['genero'])
            residente.save()
            
            # Mensaje de éxito 
            messages.success(request, f'Se ha guardado el residente "{residente.nombre}" correctamente.')
            
            
            # Redireccionar a la misma página para evitar reenvío del formulario
            return redirect('formularioResidentes')
            
    else:
        formulario = formularioResidente()
        
    return render(request, 'residentes.html', {'formulario1': formulario})



def form_invitado(request):
    if request.method == 'POST':
        formulario_inv = formularioInvitado(request.POST)
        
        if formulario_inv.is_valid():
            informacion = formulario_inv.cleaned_data
            
            invitado = Invitado(nombre=informacion['nombre'],
                                apellido=informacion['apellido'],
                                telefono=informacion['telefono'],
                                residente=informacion['residente'])
            invitado.save()
           
           # Mensaje de éxito 
            messages.success(request, f'Se ha guardado el invitado "{invitado.nombre}" correctamente. Residente: {Residente.nombre}')
            
            
                # Redireccionar a la misma página para evitar reenvío del formulario
            return redirect('formularioInvitado')
            
    else:
        formulario2 = formularioInvitado()
        
    return render(request, 'invitado.html', {'formulario2': formulario2})


def form_staff(request):
    if request.method == 'POST':
        formulario_staff = formularioStaff(request.POST)
        
        if formulario_staff.is_valid():
            informacion = formulario_staff.cleaned_data
            
            miembrostaff = Staff(   nombre=informacion['nombre'],
                                    sector=informacion['sector'],
                                    telefono=informacion['telefono'])
            miembrostaff.save()
            
            # Mensaje de éxito
            messages.success(request, f'Se ha guardado el miembro "{miembrostaff.nombre}" correctamente.')
            
            # Redireccionar a la misma página para evitar reenvío del formulario
            return redirect('formularioStaff')
            
    else:
        formulario3 = formularioStaff()
        
    return render(request, 'staff.html', {'formulario3': formulario3})

def mostrar_sectores(request):
    # Obtener todos los sectores
    sectores = Sector.objects.all()

    # Crear una lista de trabajadores asociados a cada sector
    sectores_con_trabajadores = []
    for sector in sectores:
        trabajadores = Staff.objects.filter(sector=sector)
        sectores_con_trabajadores.append({'sector': sector, 'trabajadores': trabajadores})

    return render(request, 'sectores.html', {'sectores_con_trabajadores': sectores_con_trabajadores})