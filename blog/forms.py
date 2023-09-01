from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}),  # Widget personalizado para el campo content
        max_length=256,
        required=False  # Opcional, según tus necesidades
    )

    tzone = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'custom-select'}),  # Widget personalizado para el campo tzone
        choices=Post.TZ  # Utilizamos las opciones definidas en el modelo Post
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'tzone',]