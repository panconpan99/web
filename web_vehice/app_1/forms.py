from django import forms

class FormName(forms.Form):
    nombre = forms.CharField(max_length=30)