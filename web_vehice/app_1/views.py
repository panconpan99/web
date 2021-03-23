from django.shortcuts import render
from django.http import HttpResponse
from app_1 import forms
# Create your views here.
def index(request):
    form = forms.FormName()
    return render(request,'app_1/formulario_new.html',{'form':form})

def index_1(request):
    return render(request,'app_1/index_1.html')

def index_2(request):
    return render(request,'app_1/index_2.html')

def result(request):
    return render(request, 'app_1/formulario_results.html')