from django.shortcuts import render,redirect,get_object_or_404
from .models import Persona
from .forms import PersonaForm
from django.db.models import Q # Importa esto para búsquedas avanzadas


# Create your views here.



def ficha_lista(request):
    # 1. Empezamos con TODOS
    personas = Persona.objects.all().order_by('apellidos', 'nombre')
    
    # 2. Recogemos datos del formulario (si existen)
    busqueda = request.GET.get('q')
    filtro_clase = request.GET.get('clase')
    filtro_preferencia = request.GET.get('preferencia')
    filtro_alojar_dos = request.GET.get('alojar_dos')

    # 3. Aplicamos filtros progresivamente
    if busqueda:
        # Busca en nombre O apellidos (usando Q objects)
        personas = personas.filter(
            Q(nombre__icontains=busqueda) | Q(apellidos__icontains=busqueda)
        )
    
    if filtro_clase:
        personas = personas.filter(clase__icontains=filtro_clase)
        
    if filtro_preferencia:
        personas = personas.filter(preferencia_intercambio=filtro_preferencia)
        
    if filtro_alojar_dos: # Si el checkbox está marcado
        personas = personas.filter(puedo_alojar_dos=True)

    # Contexto para la plantilla (para que el formulario recuerde lo que pusiste)
    contexto = {
        'personas': personas,
        'busqueda': busqueda,
        'filtro_clase': filtro_clase,
        'filtro_preferencia': filtro_preferencia,
        'filtro_alojar_dos': filtro_alojar_dos,
        # Truco: Pasamos las opciones del modelo para el <select>
        'opciones_preferencia': Persona.PreferenciaGenero.choices,
    }
    
    return render(request, 'ErasmusApp/ficha_lista.html', contexto)
# def ficha_lista(request):
#     personas=Persona.objects.all().order_by('apellidos','nombre')
#     apellido_filtro=request.GET.get('apellidos')
#     if apellido_filtro:
#         personas=personas.filter(apellidos__icontains=apellido_filtro)  # búsqueda case-insensitive

#     return render(request,'ErasmusApp/ficha_lista.html',{'personas':personas,'apellido_filtro':apellido_filtro})

def ficha_crear(request):
    if request.method=='POST':
        form=PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ficha_lista')
    else:
        #si es get
        form=PersonaForm()
    return render(request,'ErasmusApp/ficha_form.html',{'form':form})

def ficha_detalle(request, pk):
    persona=get_object_or_404(Persona,pk=pk)
    return render(request,'ErasmusApp/ficha_detalle.html',{'persona':persona})

def ficha_editar(request, pk):
    persona=get_object_or_404(Persona,pk=pk)
    if request.method=='POST':
        form=PersonaForm(request.POST,instance=persona)
        if form.is_valid():
            form.save()
            return redirect('ficha_lista')
    else:
        #si es get
        form=PersonaForm(instance=persona)
    return render(request,'ErasmusApp/ficha_form.html',{'form':form,'persona':persona})

def ficha_eliminar(request, pk):
    persona=get_object_or_404(Persona,pk=pk)
    if request.method=='POST':
        persona.delete()
        return redirect('ficha_lista')
    return render(request,'ErasmusApp/ficha_eliminar.html',{'persona':persona})