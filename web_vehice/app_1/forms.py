from django import forms

class Form_repr(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    correo = forms.CharField(max_length=50)
    telefono = forms.CharField(max_length=20)
    centro = forms.CharField(max_length=40)
    ciudad_centro = forms.CharField(max_length= 50)

class Form_emp(forms.Form):
    nombre=forms.CharField(max_length=30)
    rut=forms.CharField(max_length=10)

class Form_cot(forms.Form):
    cantidad=forms.IntegerField()