from django.shortcuts import render,get_object_or_404
from .models import Ingrediente
# Create your views here.

def inicio(request):

    return render(request, 'recetasApp/inicio.html')    


def ingredientes_list(request):
    ingrediente=Ingrediente.objects.all()
    return render(request, 'recetasApp/ingredientes_list.html',{'ingredientes':ingrediente}) 