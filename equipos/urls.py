from django.urls import path, include
from equipos.views import *

urlpatterns = [
    
    path('', index, name ="index"), 
    path('usuario/', Usuario, name ="usuario"), 
    path('observacion/', Observacion, name ="observacion"), 
    path('equipo/', Equipo, name ="equipo"), 
    
    #Formularios:
    path('equipo/', EquipoForm, name ="equipo"),
    path('usuario/', UsuarioForm, name ="usuario"),
    path('observacion/', ObservacionForm, name ="observacion"),     
    ]