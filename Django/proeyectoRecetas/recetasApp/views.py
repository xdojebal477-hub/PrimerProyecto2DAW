from django.shortcuts import render,get_object_or_404

from Django.proeyectoRecetas.recetasApp.forms import FiltroIngredienteForm
from .models import Ingrediente,CategoriaIngrediente
# Create your views here.

def inicio(request):

    return render(request, 'recetasApp/inicio.html')    


def ingredientes_list(request):
    ingredientes=Ingrediente.objects.all()
    categorias=CategoriaIngrediente.objects.all()
    categoria_filtro=request.GET.get('categoria')
    lactosa_filtro=request.GET.get('lactosa')
    cantidad_filtro=request.GET.get('cantidad')
    
    if  categoria_filtro:
        ingredientes=ingredientes.filter(categoria__pk=categoria_filtro)
    if  lactosa_filtro:
        ingredientes=ingredientes.filter(lactosa=True)
    if cantidad_filtro:
        ingredientes=ingredientes.filter(cantidad__cantidad=cantidad_filtro)
    
    formulario_filtro=FiltroIngredienteForm()
    return render(request, 'recetasApp/ingredientes_list.html',{'ingredientes':ingredientes, 'categorias': categorias,'lactosa_filtro': lactosa_filtro, 'cantidad_filtro': cantidad_filtro, 'formulario_filtro': formulario_filtro}) 