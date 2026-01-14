from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse_lazy
from .forms import FiltroIngredienteForm, IngredientesForm, RecetaForm
from .models import Ingrediente,CategoriaIngrediente, Recetas,IngredienteReceta
from django.forms import modelformset_factory
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView


# Create your views here.


def inicio(request):
    return render(request, 'recetasApp/inicio.html')


def ver_recetas(request):
    recetas=Recetas.objects.all()
    return render(request, 'recetasApp/ver_recetas.html', {'recetas': recetas})

def crear_receta(request):
    if request.method=='POST':
        form=RecetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_recetas')
        else:
            print(form.errors)
    else:
        form=RecetaForm()
    return render(request,'recetasApp/crear_receta.html',{'form':form})

def receta_descripcion(request, pk):
    receta = get_object_or_404(Recetas, pk=pk)
    
    if request.method == 'POST':
        ingrediente_id = request.POST.get('ingrediente_id')
        accion = request.POST.get('accion')
        if ingrediente_id:
            ingrediente = get_object_or_404(Ingrediente, pk=ingrediente_id)
            
            if accion == 'añadir':
                cantidad = request.POST.get('cantidad')
                unidad = request.POST.get('unidad_medida')
                IngredienteReceta.objects.create(receta=receta,ingrediente=ingrediente,cantidad=cantidad,unidad_medida=unidad)
            elif accion == 'eliminar':
                IngredienteReceta.objects.filter(receta=receta,ingrediente=ingrediente).delete()
                
            return redirect('receta_descripcion', pk=pk)
    
    return render(request, 'recetasApp/receta_descripcion.html', {'receta': receta, 'ingredientes': Ingrediente.objects.all()})



def relaciones(request):
    
    if request.method == 'POST':
        receta_id = request.POST.get('receta_id')
        ingrediente_id = request.POST.get('ingrediente_id')
        accion = request.POST.get('accion')
        # Obtenemos los objetos
        receta = Recetas.objects.get(pk=receta_id)
        ingrediente = Ingrediente.objects.get(pk=ingrediente_id)
        #  MANY-TO-MANY
        if accion=='añadir':
            receta.ingredientes.add(ingrediente)
        else:
            receta.ingredientes.remove(ingrediente)
        return redirect('relaciones')
    
    recetas = Recetas.objects.all()
    ingredientes = Ingrediente.objects.all()
    return render(request, 'recetasApp/relaciones.html', {'recetas': recetas, 'ingredientes': ingredientes})






# def ingredientes_list(request):
#     ingredientes=Ingrediente.objects.all()
#     categorias=CategoriaIngrediente.objects.all()
#     categoria_filtro=request.GET.get('categoria')
#     lactosa_filtro=request.GET.get('lactosa')
#     cantidad_filtro=request.GET.get('cantidad')
    
#     if  categoria_filtro:
#         ingredientes=ingredientes.filter(categoria__pk=categoria_filtro)
#     if  lactosa_filtro:
#         ingredientes=ingredientes.filter(lactosa__lactosa=True)
#     if cantidad_filtro:
#         ingredientes=ingredientes.filter(cantidad__cantidad=cantidad_filtro)
    
#     formulario_filtro=FiltroIngredienteForm()
#     return render(request, 'recetasApp/ingredientes_list.html',{'ingredientes':ingredientes, 'categorias': categorias,'lactosa_filtro': lactosa_filtro, 'cantidad_filtro': cantidad_filtro, 'formulario_filtro': formulario_filtro}) 

def creacion_masiva_ingredientes(request):
    IngredienteFormSet = modelformset_factory(Ingrediente, form=IngredientesForm, extra=5)
    
    if request.method == 'POST':
        formset = IngredienteFormSet(request.POST, queryset=Ingrediente.objects.none())
        if formset.is_valid():
            for form in formset:
                print(form.cleaned_data)
                form.save()
            return redirect('ingredientes_list')
        else:
            print(formset.errors)
    else:
        formset = IngredienteFormSet(queryset=Ingrediente.objects.none())
    
    return render(request, 'recetasApp/creacion_masiva_ingredientes.html', {'formset': formset})


# def crear_ingrediente(request):
#     if request.method == 'POST':
#         # Creamos el formulario con los datos enviados
#         form = FiltroIngredienteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('ingredientes_list')
#     else:
#         # Si es GET, mostramos el formulario vacío
#         form = FiltroIngredienteForm()
    
#     return render(request, 'recetasApp/ingrediente_form.html', {'form': form})



# def ingrediente_detalle(request, pk):
    
#     ingrediente = get_object_or_404(Ingrediente, pk=pk)
#     return render(request, 'recetasApp/ingrediente_detalle.html', {'ingrediente': ingrediente})


# def ingrediente_editar(request, pk):
    
#     ingrediente=get_object_or_404(Ingrediente,pk=pk)
#     if request.method =='POST':
#         form=FiltroIngredienteForm(request.POST,instance=ingrediente)
#         if form.is_valid():
#             form.save()
#             return redirect('ingredientes_list')
#     else:
#         form=FiltroIngredienteForm(instance=ingrediente)
#     return render(request,'recetasApp/ingrediente_form.html',{'form':form,'ingrediente':ingrediente})




def ingrediente_eliminar(request, pk):
    
    ingrediente=get_object_or_404(Ingrediente,pk=pk)
    if request.method=='POST':
        ingrediente.delete()
        return redirect('ingredientes_list')
    else:
        return render(request,'recetasApp/ingrediente_eliminar.html',{'ingrediente':ingrediente})


class IngredienteListView(ListView):
    model = Ingrediente
    template_name = 'recetasApp/ingredientes_list.html'
    context_object_name = 'ingredientes'# esto es lo mismo que poner en el render {'ingredientes':ingredientes} en las FBV  
    
    def get_queryset(self):
        
        queryset = super().get_queryset()
        
        
        categoria_filtro = self.request.GET.get('categoria')
        lactosa_filtro = self.request.GET.get('lactosa')
        cantidad_filtro = self.request.GET.get('cantidad')
        
        
        if categoria_filtro:
            queryset = queryset.filter(categoria__pk=categoria_filtro)
        if lactosa_filtro:        
            queryset = queryset.filter(lactosa__lactosa=True)
        if cantidad_filtro:
            queryset = queryset.filter(cantidad__cantidad=cantidad_filtro)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        #contexto base
        context = super().get_context_data(**kwargs)
        # datos adicionales para el template
        context['categorias'] = CategoriaIngrediente.objects.all()
        
        # Mantener los filtros en el template
        context['lactosa_filtro'] = self.request.GET.get('lactosa')
        context['cantidad_filtro'] = self.request.GET.get('cantidad')
        
        return context

class IngredienteDetailView(DetailView):
    model = Ingrediente
    template_name = 'recetasApp/ingrediente_detalle.html'
    context_object_name = 'ingrediente'


class IngredienteUpdateView(UpdateView):
    model = Ingrediente
    form_class = FiltroIngredienteForm
    template_name = 'recetasApp/ingrediente_form.html'
    success_url=reverse_lazy('ingredientes_list')
    context_object_name = 'ingrediente'

class IngredienteCreateView(CreateView):
    model = Ingrediente
    form_class = FiltroIngredienteForm
    template_name = 'recetasApp/ingrediente_form.html'
    success_url=reverse_lazy('ingredientes_list')#buscar diferencia entre reverse y reverse_lazy
    context_object_name = 'ingrediente'