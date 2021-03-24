from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpRequest
from app_1 import forms
from .forms import Form_repr,Form_emp,Form_cot
# Create your views here.
def submit(request):
    if request.method == 'POST':
        form = Form_repr(request.POST)
        print(request)
    return render(request,'app_1/formulario_new.html',{'form': form})
"""def index(request):
    if request.method == 'POST':
        form1=Form_repr(request.POST)
        form2=Form_emp(request.POST)
        if form1.is_valid() and form2.is_valid():
            return HttpResponseRedirect('/index_1/')

    return render(request,'app_1/formulario_new.html',{'form1':form1})"""

def home(request):
    return render(request,'app_1/home.html')
def index_1(request):
    return render(request,'app_1/index_1.html')

def index_2(request):
    return render(request,'app_1/index_2.html')

def result(request):
    return render(request, 'app_1/formulario_results.html')