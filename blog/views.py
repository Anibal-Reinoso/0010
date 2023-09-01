import psycopg2
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.http import HttpResponse
# from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.

CONNECTION = psycopg2.connect(
    user='postgres',
    password='admin',
    host='localhost',
    port=5432,
    database='blog',
)

def index(request):
    return HttpResponse('<div><h1>Nuestra primera aplicación!</h1></div>')

# def posteos(request):
#     """
#     Funcion para mostrar posteos de la BD
#     """
#     filtro = request.GET.get('filtro')
#     segundo_filtro = request.GET.get('segundo_filtro')

#     if filtro:
#         posts = Post.objects.filter(title__contains=filtro)
#     else:
#         posts = Post.objects.all().order_by('-author')
    
#     if segundo_filtro:
#         posts = Post.objects.filter(author=segundo_filtro)

#     context = {'posteos': posts}
#     return render(request, 'blog/posteos.html', {"context":context})

# def crear_posteo(request):
#     """
#     Formulario para creación de posteos
#     """
#     form = PostForm()
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data["title"]
#             content = form.cleaned_data["content"]
#             author = form.cleaned_data["author"]
#             tzone = form.cleaned_data["tzone"]
#             post = Post(
#                 title=title,
#                 content=content,
#                 author=author,
#                 tzone=tzone
#             )
#             post.save()
#             return redirect('posteos')
#         else:
#             return render(request, 'blog/crear_posteo.html', {"form":form})

#     return render(request, 'blog/crear_posteo.html', {"form":form})


# def modificar_posteo(request, id):
#     """
#     Funcion para modificar posteos por id
#     """
#     post = Post.objects.get(pk=id)
#     form = PostForm(instance=post)
#     if request.method == 'POST':
#         form = PostForm(request.POST, instance=post)
#         form.save()
#         return redirect('posteos')
    
#     return render(request, 'blog/modificar_posteo.html', {"form": form})

# def eliminar_posteo(request, id):
#     """
#     Funcion para eliminar posteos por id
#     """
#     post = Post.objects.get(pk=id)
#     if request.method == 'POST':
#         post.delete()
#         messages.success(request, 'Se elimino exitosamente!')
#         return redirect('posteos')


def crear_posteo(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            author = form.cleaned_data['author']
            tzone = form.cleaned_data['tzone']
            created_at = datetime.now()

            try:
                cursor = CONNECTION.cursor()

                # Insertamos los datos en la base de datos
                sSQL="INSERT INTO blog_post (title, content, author_id, created_at, tzone)"\
                "VALUES (%s,%s,%s,%s,%s);"

                cursor.execute(sSQL, (title, content, author.id, created_at, tzone))
                CONNECTION.commit()
                cursor.close()

                messages.success(request, 'Se ha creado exitosamente!')
                return redirect('posteos')
            except psycopg2.Error as error:
                print("Error al crear un posteo", error)
    return render(request, 'blog/crear_posteo.html', {"form": form})


class LoginRequiredMixin:
    """
    Verifica si el usuario esta autenticado
    """
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        print(request.user.is_authenticated)
        return super().dispatch(request,*args,**kwargs)


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/posteos.html'
    context_object_name = 'context'

    def get_queryset(self):
        queryset = super().get_queryset()
        filtro = self.request.GET.get('filtro')

        if filtro:
            queryset = queryset.filter(title__contains=filtro)
        
        return queryset

# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'blog/crear_posteo.html'
#     success_url = reverse_lazy('posteos')

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/modificar_posteo.html'
    success_url = reverse_lazy('posteos')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posteos')