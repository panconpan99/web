from django.shortcuts import render,redirect
from django.template import loader
from django.core.serializers import serialize
from django.views.generic.edit import CreateView
#from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpRequest,JsonResponse
from app_1 import forms
from .models import Empresa,Representante,Servicio,ServCot,Cotizacion
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
            return redirect('check')
    else:
        form1=repr_Form()
        form2=emp_Form()
    return render(request,'app_1/formulario.html',{'form1':form1,'form2':form2})

def check(request):

    if request.is_ajax and request.method=='GET':
        id_serv = request.GET.get['serv']
        servicio=Servicio.objects.filter(id=id_serv)
        print(id_serv)

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
            'serv':servicio,
           # 'serialize':serialize_serv,
        }
    return render(request, 'app_1/index.html',context)

def result(request):
    return render(request, 'app_1/formulario_results.html')



def test(request):
    if request.method == 'POST':
        coti=Cot_Form(request.POST)
        if coti.is_valid():
            post_cot=coti.save(commit=False)
            saved=Cotizacion.objects.create(representante=post_cot.representante)
            saved.save()
            
    else:
        coti=Cot_Form()
    return render(request,'app_1/test.html',{'servcot':coti})

