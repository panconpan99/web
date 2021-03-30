from django.shortcuts import render,redirect
from django.template import loader
from django.core.serializers import serialize
from django.http import HttpResponseRedirect, HttpRequest
from app_1 import forms
from .models import Empresa,Representante,Servicio,ServCot
from .forms import emp_Form,repr_Form,Cot_Form
import json
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
            return redirect('serv_submit')
    else:
        form1=repr_Form()
        form2=emp_Form()
    return render(request,'app_1/formulario.html',{'form1':form1,'form2':form2})

def serv_submit(request):
    servicios = Servicio.objects.values()
    cot=ServCot.objects.all()
    #serialize_serv = serialize('json',servicios)

    def get(self,request,*args,**kwargs):
       id_serv=request.GET['serv']
       servicio=Servicio.objects.filter(id=id_serv)
       print(id_serv)
        #servicio=Servicio.objects.filter(Servicio__id=id_serv)
    

    if request.method == 'POST':
        form = Cot_Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Cot_Form()
        context={
            'form':form,
            'serv':servicios,
            'servcot':cot,
           # 'serialize':serialize_serv,
        }
    return render(request, 'app_1/index.html',context)

def result(request):
    return render(request, 'app_1/formulario_results.html')

def test(request):
    servicios = Servicio.objects.all()
    return render(request,'app_1/test.html',{'serv':servicios})
