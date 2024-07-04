from django.shortcuts import render, redirect
# Modelos:
from equipos.models import Equipo, Usuario, Observacion
# Formularios:
from equipos.forms import *

# Create your views here.

def index(request):
    return render(request, "equipos/index.html") 

def equipos(request):
    search_form = EquipoSearchForm(request.GET or None)
    search_term = ''

    if search_form.is_valid():
        search_term = search_form.cleaned_data['search_term']

    if request.method == "POST":
        EquipoForm = EquipoForm(request.POST)
        if EquipoForm.is_valid():
            EquipoForm.save()
            return redirect('equipo')
    else:
        EquipoForm = EquipoForm()

    equipos = Equipo.objects.filter(nombre__icontains=search_term) if search_term else Equipo.objects.all()

    contexto = {
        "equipoForm": EquipoForm,
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
        UsuarioForm = UsuarioForm(request.POST)
        if UsuarioForm.is_valid():
            UsuarioForm.save()
            return redirect('usuario')
    else:
        UsuarioForm = UsuarioForm()

    usuarios = Usuario.objects.filter(nombre__icontains=search_term) if search_term else Usuario.objects.all()

    contexto = {
        "UsuarioForm": UsuarioForm,
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
        ObservacionForm = ObservacionForm(request.POST)
        if ObservacionForm.is_valid():
            ObservacionForm.save()
            return redirect('observacion')
    else:
        ObservacionForm = ObservacionForm()

    observaciones = Observacion.objects.filter(nombre__icontains=search_term) if search_term else Observacion.objects.all()

    contexto = {
        "ObservacionForm": ObservacionForm,
        "observaciones": observaciones,
        "search_form": search_form,
    }
    return render(request, "equipos/observacion.html", contexto)