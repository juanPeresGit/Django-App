from django.shortcuts import render
from blog.models import Post, Categoria
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def blog(request):
    posts=Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})


#funtion: muestar las categorias por id de cada autor y
# muestra los post de acuerdo a la categoria
@login_required
def categoria(request, categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request, 'blog/categoria.html', {'categoria': categoria, 'posts': posts})

