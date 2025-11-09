from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
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