from django.db import models
from django.utils import timezone
import datetime
from django.db.models import Max

# Create your models here.
class Empresa(models.Model):
    Nombre=models.CharField(max_length=30)
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
    region=models.CharField(max_length=4,choices=region_choices)
    def __str__(self):
        return self.Nombre

class Representante(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    correo=models.EmailField()
    telefono=models.CharField(max_length=20)
    centro=models.CharField(max_length=40)
    ciudad_centro=models.CharField(max_length=50)
    empresa=models.ForeignKey(Empresa,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre +" "+ self.apellido+ "/" +self.centro

class Servicio(models.Model):
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=255)
    image_ruta=models.ImageField(upload_to='static/photos')
    precio= models.FloatField(max_length=30,default=0)

    def __str__(self):
        return self.nombre

class Cotizacion(models.Model):
    fecha=models.DateField(auto_now=True, auto_now_add=False)
    representante=models.ForeignKey(Representante,on_delete=models.CASCADE)
    servicio=models.ManyToManyField(Servicio,through='ServCot')
    
    def __str__(self):
        return str(self.id)+" "+str(self.representante.nombre)
    


class ServCot(models.Model):
    servicio=models.ForeignKey(Servicio,on_delete=models.CASCADE)
    cotizacion=models.ForeignKey(Cotizacion,on_delete=models.CASCADE)
    nuevo_precio=models.FloatField(max_length=30)
    cantidad=models.IntegerField(default=1)

    def __str__(self):
        return str(self.cotizacion.id)+"-"+str(self.servicio.nombre)
    

