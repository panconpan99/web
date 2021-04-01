from django import forms
from .models import Representante,Empresa,Servicio,ServCot,Cotizacion
from django.forms import ModelForm

class emp_Form(ModelForm):
    class Meta:
        fields='__all__'
        model=Empresa
    
    def __init__(self, *args, **kwargs):
        super(emp_Form,self).__init__(*args, **kwargs)
        self.fields['rut'].widget.attrs['placeholder']='12345678-9'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['required'] ='True'

    

class repr_Form(forms.ModelForm):
    
    class Meta:
        fields = ('nombre','apellido','correo','telefono','centro','ciudad_centro',)
        model = Representante
    
    def __init__(self, *args, **kwargs):
        super(repr_Form,self).__init__(*args, **kwargs)
        self.fields['correo'].widget.attrs['placeholder']='email@address.cl'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
   
class Cot_Form(forms.ModelForm):
    class Meta:
        fields= ('representante','servicio')
        model=Cotizacion

    def __init__(self, *args, **kwargs):
        super(Cot_Form,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
#class cotserv_Form(form.ModelForm):



        
