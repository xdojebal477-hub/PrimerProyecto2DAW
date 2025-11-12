from django.shortcuts import redirect,render, get_object_or_404
from .models import Post,Autor
from django.db.models import Count
from .forms import Autorform
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

def autor_nuevo(request):
    if request.method =='POST':
        form=Autorform(request.POST)
        if form.is_valid():
            #alamceno en BD
            nombre=form.cleaned_data['nombre']
            email=form.cleaned_data['email']
            
            Autor.objects.create(nombre=nombre,email=email)
            return redirect('lista_autores')

    else:
        form=Autorform()
    
    return render (request,'blog/autor_nuevo.html',{'form':form})