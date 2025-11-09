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
    
    """
    #seccion=Post.objects.all()
    context={
        'lo que sea ': seccion
    }
    """
    context=Post.objects.all()
    
    return render(request,'blog/principal.html',{'posts':context})

def detalle_post(request,pk):
    context=get_object_or_404(Post, pk=pk)
    return render(request,'blog/detalle_post.html',{'post':context})