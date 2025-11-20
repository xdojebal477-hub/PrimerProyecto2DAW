from django.shortcuts import redirect, render,get_object_or_404

from .forms import FiltroIngredienteForm
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
        ingredientes=ingredientes.filter(lactosa__lactosa=True)
    if cantidad_filtro:
        ingredientes=ingredientes.filter(cantidad__cantidad=cantidad_filtro)
    
    formulario_filtro=FiltroIngredienteForm()
    return render(request, 'recetasApp/ingredientes_list.html',{'ingredientes':ingredientes, 'categorias': categorias,'lactosa_filtro': lactosa_filtro, 'cantidad_filtro': cantidad_filtro, 'formulario_filtro': formulario_filtro}) 


def crear_ingrediente(request):
    if request.method == 'POST':
        # Creamos el formulario con los datos enviados
        form = FiltroIngredienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredientes_list')
    else:
        # Si es GET, mostramos el formulario vacío
        form = FiltroIngredienteForm()
    
    return render(request, 'recetasApp/ingrediente_form.html', {'form': form})


def ingrediente_detalle(request, pk):
    
    ingrediente = get_object_or_404(Ingrediente, pk=pk)
    return render(request, 'recetasApp/ingrediente_detalle.html', {'ingrediente': ingrediente})


def ingrediente_editar(request, pk):
    
    ingrediente=get_object_or_404(Ingrediente,pk=pk)
    if request.method =='POST':
        form=FiltroIngredienteForm(request.POST,instance=ingrediente)
        if form.is_valid():
            form.save()
            return redirect('ingredientes_list')
    else:
        form=FiltroIngredienteForm(instance=ingrediente)
    return render(request,'recetasApp/ingrediente_form.html',{'form':form,'ingrediente':ingrediente})

def ingrediente_eliminar(request, pk):
    
    ingrediente=get_object_or_404(Ingrediente,pk=pk)
    if request.method=='POST':
        ingrediente.delete()
        return redirect('ingredientes_list')
    else:
        return render(request,'recetasApp/ingrediente_eliminar.html',{'ingrediente':ingrediente})