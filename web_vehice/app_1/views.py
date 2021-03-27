from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponseRedirect, HttpRequest
from app_1 import forms
from .models import Empresa,Representante
from .forms import emp_Form,repr_Form
# Create your views here.

def submit(request):
    if request.method == 'POST':
        form1 = repr_Form(request.POST)
        form2 = emp_Form(request.POST)
        checkbox = request.POST.__contains__('ref_ppl')
        if form1.is_valid() and form2.is_valid():
            post_emp = form2.save(commit=False)
            post_repr = form1.save(commit=False)
            finder,created=Empresa.objects.get_or_create(Nombre=post_emp.Nombre)
            post_repr.id_emp_id=finder.id
            finder.save()
            post_repr.save()
            context={
                'checkbox':checkbox,
            }
            return render(request,'app_1/index.html',context)
    else:
        form1=repr_Form()
        form2=emp_Form()
    return render(request,'app_1/formulario_test.html',{'form1':form1,'form2':form2})

def result(request):
    return render(request, 'app_1/formulario_results.html')
