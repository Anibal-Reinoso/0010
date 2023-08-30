from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib import messages

# Create your views here.

def index(request):
    return HttpResponse('<div><h1>Nuestra primera aplicación!</h1></div>')

def posteos(request):
    """
    Funcion para mostrar posteos de la BD
    """
    filtro = request.GET.get('filtro')
    segundo_filtro = request.GET.get('segundo_filtro')

    if filtro:
        posts = Post.objects.filter(title__contains=filtro)
    else:
        posts = Post.objects.all().order_by('-author')
    
    if segundo_filtro:
        posts = Post.objects.filter(author=segundo_filtro)

    context = {'posteos': posts}
    return render(request, 'blog/posteos.html', {"context":context})

def crear_posteo(request):
    """
    Formulario para creación de posteos
    """
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            author = form.cleaned_data["author"]
            tzone = form.cleaned_data["tzone"]
            post = Post(
                title=title,
                content=content,
                author=author,
                tzone=tzone
            )
            post.save()
            return redirect('posteos')
        else:
            return render(request, 'blog/crear_posteo.html', {"form":form})

    return render(request, 'blog/crear_posteo.html', {"form":form})


def modificar_posteo(request, id):
    """
    Funcion para modificar posteos por id
    """
    post = Post.objects.get(pk=id)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        form.save()
        return redirect('posteos')
    
    return render(request, 'blog/modificar_posteo.html', {"form": form})

def eliminar_posteo(request, id):
    post = Post.objects.get(pk=id)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Se elimino exitosamente!')
        return redirect('posteos')