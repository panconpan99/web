from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class represante(models.Model):
    repr_name=models.CharField(max_length=30,unique=True)
    repr_apellido=models.CharField(max_length=30,unique=True)
    repr_correo=models.EmailField(max_length=50,unique=True)
    telefono=models.CharField(max_length=20)
    repr_centro=models.CharField(max_length=40)
    repr_dir_centro=models.CharField(max_length=50)
    id_repr=models.IntegerField(primary_key=True)

    def __str__(self):
        return "%s %s" % (self.repr_name, self.repr_apellido)

class cotizacion(models.Model):
    cantidad=models.IntegerField()
    fecha=models.DateField(auto_now=True, auto_now_add=False)
    id_cot=models.IntegerField(primary_key=True)

class servicio(models.Model):
    id_servicio=models.IntegerField(primary_key=True)
    descripcion=models.CharField(max_length=255)
    serv_name=models.CharField(max_length=30)
    image_ruta=models.ImageField(upload_to='servicio')


class repr_cot(models.Model):
    repr_id=models.ForeignKey(represante,on_delete=models.CASCADE)
    cot_id=models.ForeignKey(cotizacion,on_delete=models.CASCADE)

class serv_cot(models.Model):
    id_cot=models.ForeignKey(cotizacion,on_delete=models.CASCADE)
    id_servicio=models.ForeignKey(servicio, on_delete=models.CASCADE)
