from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Empresa(models.Model):
    nombre=models.CharField(max_length=30)
    rut=models.CharField(max_length=10)
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
    region=models.CharField(max_length=4,choices=region_choices,default="")
    def __str__(self):
        return self.nombre

class Representante(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    correo=models.EmailField()
    telefono=models.CharField(max_length=20)
    centro=models.CharField(max_length=40)
    ciudad_centro=models.CharField(max_length=50)
    id_emp=models.ForeignKey(Empresa,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre +" "+ self.apellido+ "/" +self.centro

class Cotizacion(models.Model):
    fecha=models.DateField(auto_now=True, auto_now_add=False)
    id_repr=models.ForeignKey(Representante,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)+" "+str(self.fecha)



class Servicio(models.Model):
    descripcion=models.CharField(max_length=255)
    nombre=models.CharField(max_length=30,)
    image_ruta=models.ImageField(upload_to='servicio')
    id_cot=models.ManyToManyField(Cotizacion, through='Serv_cot')
    precio= models.FloatField(max_length=30,default=0)

    def __str__(self):
        return self.nombre

class Serv_cot(models.Model):
    id_ser=models.ForeignKey(Servicio,on_delete=models.CASCADE)
    id_cot=models.ForeignKey(Cotizacion,on_delete=models.CASCADE)
    nuevo_precio=models.FloatField(max_length=30)
    cantidad=models.IntegerField(default=1)

    def __str__(self):
        return self.id
    

