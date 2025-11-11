from django.shortcuts import render, get_object_or_404
from .models import Post,Autor
from django.db.models import Count

# Create your views here.


def lista_autores(request):
    # Consulta con agregación (annotate()) para contar cuántos posts tiene cada autor.
    # En el modelo Post usamos related_name='posts', por eso la relación inversa es 'posts',
    # no 'post'. Usar la clave equivocada provocaba FieldError.
    autores = Autor.objects.annotate(num_posts=Count('posts'))
    return render(request, 'blog/autores.html', {'autores': autores})

def principal(request):
    
    entrada=Post.objects.all()
    contexto={'entradas':entrada,'autores':Autor.objects.all()}
    return render(request,'blog/principal.html',contexto)

def detalle_post(request,pk):
    context=get_object_or_404(Post, pk=pk)
    return render(request,'blog/detalle_post.html',{'post':context})

def autor_post(request,autor_pk):
    # context=get_object_or_404(Autor,pk=pk)
    entrada=Post.objects.filter(autor=autor_pk)
    autor=get_object_or_404(Autor,pk=autor_pk)
    contexto={'entradas':entrada,'autor':autor}
    return render(request,'blog/autor_post.html',contexto)