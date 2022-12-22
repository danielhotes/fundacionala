from .models import Noticia, Comentario
from django import forms

class FormComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['comentario']
        widgets = {
            'comentario' : forms.Textarea(attrs={'class':'form-control'}),         
        }

