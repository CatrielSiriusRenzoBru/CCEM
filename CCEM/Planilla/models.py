from django.db import models

# Create your models here.

class Planilla (models.Model):
    Dia = models.DateTimeField(auto_now_add=True)
    Propietario = models.CharField(max_length=100)
    Manzana = models.IntegerField(null=True ,blank=True)
    Lote = models.IntegerField(null=True ,blank=True)
    Usuario = models.CharField(max_length=100, null=True ,blank=True)
    cant = models.IntegerField(default=1)
    Aprobado = models.BooleanField(default=False)