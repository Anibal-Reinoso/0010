from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(request):
    content = HttpResponse('<div><h1>Nuestra primera aplicación!</h1></div>')
    data = {"name": "Juanito", "edad": 10}

    context = {'content': content,
               'data': data}
    
    return render(request=request, template_name='index.html', context={'context':context})

def posteos(request):
    """
    Funcion para mostrar posteos de la BD
    """
    filtro = request.GET.get('filtro')

    if filtro:
        posts = Post.objects.filter(title__contains=filtro)
    else:
        posts = Post.objects.all()

    context = {'posteos': posts}
    return render(request, 'blog/posteos.html', {"context":context})


