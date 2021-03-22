from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'app_1/formulario_new.html')

def index_1(request):
    return render(request,'app_1/index_1.html')