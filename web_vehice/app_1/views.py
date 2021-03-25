from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponseRedirect, HttpRequest
from app_1 import forms
from .forms import emp_Form,repr_Form
# Create your views here.

def submit(request):
    if request.method == 'POST':
        form1 = repr_Form(request.POST)
        form2 = emp_Form(request.POST)
        checkbox = request.POST.__contains__('test')
        if form1.is_valid() and form2.is_valid():
            post_repr = form1.save(commit=False)
            post_emp = form2.save()
            if post_repr.id_emp_id is None:
                post_repr.id_emp_id=post_emp.id
            post_repr.save()
            post_emp.save()
            return render(request,'app_1/index.html',{'checkbox':checkbox})
    else:
        form1=repr_Form()
        form2=emp_Form()
    return render(request,'app_1/formulario_test.html',{'form1':form1,'form2':form2})

def home(request):
    return render(request,'app_1/formulario_test.html')

def index_1(request):
    return render(request,'app_1/index_1.html')

def index_2(request):
    return render(request,'app_1/index_2.html')

def result(request):
    return render(request, 'app_1/formulario_results.html')
