from django import forms
from .models import *

class FiltroIngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['nombre','categoria', 'lactosa', 'cantidad']


class IngredientesForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['nombre','categoria', 'lactosa', 'cantidad']

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Recetas
        fields = ['nombre', 'descripcion']