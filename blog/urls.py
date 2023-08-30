from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('posteos/', views.posteos, name='posteos'),
    path('crear_posteo/', views.crear_posteo, name='crear_posteo'),
    path('modificar_posteo/<id>/', views.modificar_posteo, name='modificar_posteo'),
    path('eliminar_posteo/<id>/', views.eliminar_posteo, name='eliminar_posteo'),
]
