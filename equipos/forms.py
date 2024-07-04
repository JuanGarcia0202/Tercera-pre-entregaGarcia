from django import forms
from equipos.models import Equipo, Usuario, Observacion

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['marca', 'modelo', 'serie', 'placa']

class EquipoSearchForm(forms.Form):
    search_term = forms.CharField(max_length=100, required=False, label='Buscar Equipo')

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'ubicacion']

class UsuarioSearchForm(forms.Form):
    search_term = forms.CharField(max_length=100, required=False, label='Buscar Usuario')
    
class ObservacionForm(forms.ModelForm):
    class Meta:
        model = Observacion
        fields = ['observacion']

class ObservacionSearchForm(forms.Form):
    search_term = forms.CharField(max_length=100, required=False, label='Buscar Observacion')