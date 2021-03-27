from django import forms
from .models import Representante,Empresa,Servicio,Serv_cot 
from django.forms import ModelForm

class emp_Form(ModelForm):
    class Meta:
        fields='__all__'
        model=Empresa
    
    def __init__(self, *args, **kwargs):
        super(emp_Form,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['required'] ='True'

    

class repr_Form(forms.ModelForm):
    
    class Meta:
        fields = ('nombre','apellido','correo','telefono','centro','ciudad_centro',)
        model = Representante
    
    def __init__(self, *args, **kwargs):
        super(repr_Form,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
   


