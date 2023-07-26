"""
URL configuration for AppCoder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import inicio, form_residentes, form_invitado, form_staff, mostrar_sectores, busqueda_resultados
urlpatterns = [
    path('', inicio, name="inicio"),
    path('formularioResidentes/', form_residentes, name="formularioResidentes"),
    path('formularioInvitado/', form_invitado, name="formularioInvitado"),
    path('formularioStaff/', form_staff, name="formularioStaff"),
    path('mostrarSectores/', mostrar_sectores, name="mostrarSectores"),
    path('busquedaResultados/', busqueda_resultados, name='busquedaResultados'),

]
