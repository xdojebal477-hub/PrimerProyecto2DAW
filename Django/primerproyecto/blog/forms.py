from django import forms
from .models import Autor
class Autorform(forms.ModelForm):
    nombre=forms.CharField(max_length=100)
    email=forms.EmailField()
    
class AutorModelform(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'email']