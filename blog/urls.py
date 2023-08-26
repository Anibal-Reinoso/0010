from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('posteos/', views.posteos, name='posteos'),
]
