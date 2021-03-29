from django.contrib import admin
from django.urls import path
from app_1 import views

urlpatterns = [
    path('',views.home,name='formulario_test'),
    path('',views.index, name ='submit'),
    path('',views.result, name='result'),
]