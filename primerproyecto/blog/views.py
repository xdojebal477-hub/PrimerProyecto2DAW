from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.
def inicio(request):
    # contexto={
    #     'titulo':'Mi primera entrada',
    #     'autor':'Daniel Ojeda Balsera',
    # }
    entradas=Post.objects.all()
    entradasAutor=Post.objects.filter(autor__startswith='D')
    entradasID=Post.objects.filter(id='2')
    contexto={
        'entradas':entradas,
        'entradasAutor':entradasAutor,
        'entradasID':entradasID
    }
    return render(request,'blog/inicio.html',contexto)

def detalle_post(request,pk):
    # entrada=Post.objects.get(pk=pk)
    # contexto={
    #     'entrada':entrada
    # }
    contexto=get_object_or_404(Post,pk=pk)
    return render(request,'blog/detalle_post.html',contexto)
