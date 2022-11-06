from django.db import models
from django.db.models import Model

# Create your models here.

class Familiares(models.Model):
    nombre = models.CharField(max_length=30)
    relacion = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()


    def __str__(self):
        return self.relacion
    
