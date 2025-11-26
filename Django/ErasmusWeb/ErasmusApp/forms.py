from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'  # Usamos todos los campos del modelo
        
        
        widgets = {
            #  Hacemos que salga un calendario real en el navegador
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            
            #  Convertimos los desplegables en "Bolitas" (Radio Buttons), 
            'sexo': forms.RadioSelect(),
            'preferencia_intercambio': forms.RadioSelect(),
            
            #  Ajustamos el tamaño de las cajas de texto grandes
            'caracter': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Soy una persona...'}),
            'deportes': forms.Textarea(attrs={'rows': 2}),
            'musica': forms.Textarea(attrs={'rows': 2}),
            'otros_hobbies': forms.Textarea(attrs={'rows': 2}),
            'problemas_salud': forms.Textarea(attrs={'rows': 2}),
        }
        


