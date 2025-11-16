from django.shortcuts import render,get_object_or_404
from .models import Cliente,PC

# Create your views here.
def principal(request):
    return render(request,'blog/principal.html')


def ver_clientes(request):
    clientes=Cliente.objects.all()
    return render(request,'blog/ver_clientes.html',{'clientes':clientes})

def ver_pcs_cliente(request,cliente_pk):
    cliente=get_object_or_404(Cliente,pk=cliente_pk)
    pcs=cliente.pcs.all()
    
    return render(request,'blog/pcs_cliente.html',{'cliente':cliente,'pcs':pcs})

def especificaciones_pc(request,pc_pk):
    pc=get_object_or_404(PC,pk=pc_pk)
    especificaciones={
        'cpu':pc.cpu,
        'ram':pc.ram,
        'ssd':pc.ssd,
        'gpu':pc.gpu
    }
    return render(request,'blog/especificaciones_pc.html',{'pc':pc,'especificaciones':especificaciones})