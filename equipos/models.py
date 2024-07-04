from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=60)
    
class Equipo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    serie = models.CharField(max_length=10)
    placa = models.CharField(max_length=50)

class Observacion(models.Model):
    observacion = models.CharField(max_length=50)