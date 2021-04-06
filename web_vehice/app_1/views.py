from django.shortcuts import render,redirect
from django.template import loader
from django.core.serializers import serialize
from django.views.generic.edit import CreateView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpRequest,JsonResponse
from app_1 import forms
from .models import Empresa,Representante,Servicio,ServCot,Cotizacion
from .forms import emp_Form,repr_Form,Cot_Form
import json
from twisted.names.dns import NULL
# Create your views here.

def home(request):
    return render(request,'app_1/home.html')


def submit(request):
    if request.method == 'POST':
        form1 = repr_Form(request.POST)
        form2 = emp_Form(request.POST)
        if form1.is_valid() and form2.is_valid():
            post_emp = form2.save(commit=False)
            post_repr = form1.save(commit=False)
            finder,created=Empresa.objects.get_or_create(Nombre=post_emp.Nombre)
            post_repr.empresa_id=finder.id
            finder.save()
            post_repr.save()
            return redirect('servsubmit')
    else:
        form1=repr_Form()
        form2=emp_Form()
    return render(request,'app_1/formulario.html',{'form1':form1,'form2':form2})

def finish(request):
    return render(request,'app_1/formulario_results.html')


@csrf_exempt
def servsubmit(request):
    serv= Servicio.objects.all()
    cot=[Cotizacion.objects.latest('id')]
    repre=Representante.objects.all()
    repreid=request.POST.get("id")
    if request.method == 'POST' and repreid != None:
        print(repreid)
        try:
            coti=Cotizacion(representante_id=repreid)
            coti.save()
            cot=[Cotizacion.servicio.latest('id')]
            #no salen los mensajes
            coti_data={"id":coti.id,"representante_id":coti.representante.id,"error":False,"ErrorMessage":"Cotización Creada"}
            return JsonResponse(coti_data,safe=False)
        except:
            print("error")
            coti_data={"error":True,"errorMessage":"Cotización fallida"}
            return JsonResponse(coti_data,safe=False)
    
    return render(request,'app_1/test.html',{'repre':repre,'serv':serv,'cot':cot})


@csrf_exempt
def insertserv(request):
    idserv= request.POST.get("idserv")
    servcount= request.POST.get("servcount")
    servprecio = request.POST.get("servprecio")
    cot=Cotizacion.objects.latest('id')
    try:
        servicio=Servicio.objects.get(id=idserv)
        #si hay precio vacio
        if servprecio == "":
            servprecio = servicio.precio 
        cot.servicio.add(servicio, through_defaults={'cantidad' : servcount,'nuevo_precio' : servprecio})
        Cot=cot.servicio.latest("id")
        serv_data={"nombre":Cot.nombre,"descripcion":Cot.descripcion,"cantidad":servcount,"precio":servprecio,"error":False,"ErrorMessage":"Servicio Creado"}
        return JsonResponse(serv_data,safe=False)
    except Exception as e:
        print(e)
        serv_data={"error":True,"ErrorMessage":"error"}
        return JsonResponse(serv_data,safe=False)


    

    

