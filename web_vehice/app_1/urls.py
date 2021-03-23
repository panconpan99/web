from django.contrib import admin
from django.urls import path
from app_1 import views

urlpatterns = [
    path('',views.index_1, name='index_1'),
    path('',views.index_2, name='index_2'),
    path('',views.result, name='result'),
]