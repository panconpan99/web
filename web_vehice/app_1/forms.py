from django import forms

class Form_repr(forms.Form):
    nombre = forms.CharField(max_length=30, label='name_ppl_new')
    apellido = forms.CharField(max_length=30, label='lastname_ppl_new')
    correo = forms.CharField(max_length=50, label='email_ppl_new')
    telefono = forms.CharField(max_length=20, label= 'tel_ppl_new')
    centro = forms.CharField(max_length=40, label='place_ppl_new')
    ciudad_centro = forms.CharField(max_length= 50, label='place_dir_new')
    
    
    def __init__(self, *args, **kwargs):
        super(Form_repr, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['required'] ='True'
    
    #faltaria agregar los errores de validacion


class Form_emp(forms.Form):
    nombre=forms.CharField(max_length=30,label='enpr_ppl_new')
    rut=forms.CharField(max_length=10,label= 'rut_enp_new')
    
    def __init__(self, *args, **kwargs):
        super(Form_emp, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['required'] ='True'

class Form_cot(forms.Form):
    cantidad=forms.IntegerField()