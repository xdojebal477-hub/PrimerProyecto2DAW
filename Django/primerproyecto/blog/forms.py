from django import forms

class Autorform(forms.Form):
    nombre = forms.CharField(max_length=60, label="Nombre autor:")
    
    email = forms.EmailField()