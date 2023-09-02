from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    TZ = [
        ("EU", "EUROPE"),
        ("AS", "ASIA"),
        ("US", "UNITED STATES"),
    ]
    title = models.CharField(max_length=100, verbose_name='Titulo del Posteo')
    content = models.TextField(verbose_name='Contenido del Posteo', max_length=256, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author del Posteo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion del Post')
    tzone = models.CharField(choices=TZ, verbose_name='Zona Horaria', max_length=10)

    class Meta:
        verbose_name = "Posteo"
    
    def __str__(self):
        return self.title + ' - ' + str(self.created_at)


class Comment(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titutlo del Comentario', null=True)
    post = models.ForeignKey('Post', related_name="post", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha del comentario")

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
    
    def __str__(self):
        return self.title
    