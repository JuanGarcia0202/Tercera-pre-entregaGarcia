from django.shortcuts import render, redirect
#Modelos:
from equipos.models import Equipo, Observacion, Usuario


#Formularios:
from equipos.forms import *


def index(request):
    return render(request, "equipos/index.html") 

def equipos(request):
    search_form = EquipoSearchForm(request.GET or None)
    search_term = ''

    if search_form.is_valid():
        search_term = search_form.cleaned_data['search_term']

    if request.method == "POST":
        equiposForm = EquipoForm(request.POST)
        if equiposForm.is_valid():
            equiposForm.save()
            return redirect('equipos')
    else:
        equiposForm = EquipoForm()

    equipos = Equipo.objects.filter(nombre__icontains=search_term) if search_term else Equipo.objects.all()

    contexto = {
        "equiposForm": equiposForm,
        "equipos": equipos,
        "search_form": search_form,
    }
    return render(request, "equipos/equipo.html", contexto)

def usuarios(request):
    search_form = UsuarioSearchForm(request.GET or None)
    search_term = ''

    if search_form.is_valid():
        search_term = search_form.cleaned_data['search_term']

    if request.method == "POST":
        usuariosForm = UsuarioForm(request.POST)
        if usuariosForm.is_valid():
            usuariosForm.save()
            return redirect('usuarios')
    else:
        usuariosForm = UsuarioForm()

    usuarios = Usuario.objects.filter(nombre__icontains=search_term) if search_term else Usuario.objects.all()

    contexto = {
        "usuarioForm": usuariosForm,
        "usuarios": usuarios,
        "search_form": search_form,
    }
    return render(request, "equipos/usuario.html", contexto)

def observaciones(request):
    search_form = ObservacionSearchForm(request.GET or None)
    search_term = ''

    if search_form.is_valid():
        search_term = search_form.cleaned_data['search_term']

    if request.method == "POST":
        observacionesForm = ObservacionForm(request.POST)
        if observacionesForm.is_valid():
            observacionesForm.save()
            return redirect('observaciones')
    else:
        observacionesForm = ObservacionForm()

    observaciones = Observacion.objects.filter(nombre__icontains=search_term) if search_term else Observacion.objects.all()

    contexto = {
        "observacionesForm": observacionesForm,
        "observaciones": observaciones,
        "search_form": search_form,
    }
    return render(request, "equipos/observacion.html", contexto)
