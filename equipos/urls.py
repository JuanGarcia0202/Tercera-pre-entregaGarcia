from django.urls import path, include
from equipos.views import *

urlpatterns = [
    
    path('', index, name ="index"), 
    path('usuario/', usuarios, name ="usuario"), 
    path('observacion/', observaciones, name ="observacion"), 
    path('equipo/', equipos, name ="equipo"), 
    
    #Formularios:
    path('equipo/', EquipoForm, name ="equipo"),
    path('usuario/', UsuarioForm, name ="usuario"),
    path('observacion/', ObservacionForm, name ="observacion"),     
]
