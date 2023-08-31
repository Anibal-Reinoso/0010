from django.urls import path
from . import views
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('index/', views.index, name='index'),
    # path('posteos/', views.posteos, name='posteos'),
    path('posteos/', PostListView.as_view(), name='posteos'),
    # path('crear_posteo/', views.crear_posteo, name='crear_posteo'),
    path('crear_posteo/', PostCreateView.as_view(), name='crear_posteo'),
    # path('modificar_posteo/<id>/', views.modificar_posteo, name='modificar_posteo'),
    path('modificar_posteo/<pk>/', PostUpdateView.as_view(), name='modificar_posteo'),
    # path('eliminar_posteo/<id>/', views.eliminar_posteo, name='eliminar_posteo'),
    path('eliminar_posteo/<pk>/', PostDeleteView.as_view(), name='eliminar_posteo'),
]
