from django.db import models
from django.utils import timezone
import datetime
from django.db.models import Max

# Create your models here.
class Empresa(models.Model):
    Nombre=models.CharField(max_length=30)
    rut=models.CharField(max_length=10)
    pais_choices=[
        ('CH','Chile'),
        ('AR','Argentina'),
        ('EU','Estados Unidos'),
        ('CA','Canada'),
        ('ES','España'),
        ('PO','Portugal'),
        ('AU','Australia'),
        ('SW','Suecia'),
        ('NO','Noruega'),
    ]
    Pais=models.CharField(max_length=4,choices=pais_choices)
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
    imagen_ruta=models.ImageField(upload_to='static/photos')
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
    cantidad=models.IntegerField(default=1)
    nuevo_precio=models.FloatField(max_length=30)

    def __str__(self):
        return str(self.cotizacion.id)+"-"+str(self.servicio.nombre)
    

