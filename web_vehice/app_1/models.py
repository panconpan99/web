from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Empresa(models.Model):
    nombre=models.CharField(max_length=30,unique=True)
    rut=models.CharField(max_length=10,unique=True)
    region_choices=[
        ('XV','Región de Arica y Parinacota'),
        ('I','Región de Tarapacá'),
        ('II','Región de Antofagasta'),
        ('III','Región de Atacama'),
        ('IV','Región de Coquimbo'),
        ('V','Región de Valparaíso'),
        ('RM','Región Metropolitana de Santiago'),
        ('VI','Región del Libertador General Bernardo OHiggins'),
        ('VII','Región del Maule'),
        ('XVI','Región del Ñuble'),
        ('VIII','Región del Biobío'),
        ('IX','Región de La Araucania'),
        ('XIV','Región de Los Ríos'),
        ('X','Región de Los Lagos'),
        ('XI','Región de Aysén del General Carlos Ibáñez del Campo'),
        ('XII','Región de Magallanes y la Antártica Chilena'),
    ]
    region=models.CharField(max_length=4,choices=region_choices,default="",unique=True)

class Representante(models.Model):
    nombre=models.CharField(max_length=30,unique=True)
    apellido=models.CharField(max_length=30,unique=True)
    correo=models.EmailField(unique=True)
    telefono=models.CharField(max_length=20,unique=True)
    centro=models.CharField(max_length=40,unique=True)
    ciudad_centro=models.CharField(max_length=50,unique=True)
    id_emp=models.ForeignKey(Empresa,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Cotizacion(models.Model):
    cantidad=models.IntegerField(unique=True)
    fecha=models.DateField(auto_now=True, auto_now_add=False)
    id_repr=models.ForeignKey(Representante,on_delete=models.CASCADE)


class Servicio(models.Model):
    descripcion=models.CharField(max_length=255)
    nombre=models.CharField(max_length=30,unique=True)
    image_ruta=models.ImageField(upload_to='servicio')
    id_cot=models.ManyToManyField(Cotizacion, through='Serv_cot')
    precio= models.FloatField(max_length=30,default=0)

class Serv_cot(models.Model):
    id_ser=models.ForeignKey(Servicio,on_delete=models.CASCADE)
    id_cot=models.ForeignKey(Cotizacion,on_delete=models.CASCADE)
    nuevo_precio=models.FloatField(max_length=30,default=0)

