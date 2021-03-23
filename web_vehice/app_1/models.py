from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class representante(models.Model):
    nombre=models.CharField(max_length=30,unique=True)
    apellido=models.CharField(max_length=30,unique=True)
    corre=models.EmailField(max_length=50,unique=True)
    telefono=models.CharField(max_length=20)
    centro=models.CharField(max_length=40)
    dir_centro=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class cotizacion(models.Model):
    cantidad=models.IntegerField()
    fecha=models.DateField(auto_now=True, auto_now_add=False)

class servicio(models.Model):
    descripcion=models.CharField(max_length=255)
    nombre=models.CharField(max_length=30)
    image_ruta=models.ImageField(upload_to='servicio')


class repr_cot(models.Model):
    repr_id=models.ForeignKey(representante,on_delete=models.CASCADE)
    cot_id=models.ForeignKey(cotizacion,on_delete=models.CASCADE)

class serv_cot(models.Model):
    id_cot=models.ForeignKey(cotizacion,on_delete=models.CASCADE)
    id_servicio=models.ForeignKey(servicio, on_delete=models.CASCADE)
