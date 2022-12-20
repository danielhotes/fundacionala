from .models import Noticia, Comentario
from django import forms

# class AgregarNoticiaForm(forms.ModelForm):

#     class Meta:
#         model = Noticia
#         fields = '__all__'

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ('titulo', 'subtitulo', 'texto', 'activo', 'categoria', 'imagen', 'publicado', 'autor')

        widgets = {
            'titulo' : forms.TextInput(attrs={'class':'form-control'}),
            'subtitulo' : forms.TextInput(attrs={'class':'form-control'}),
            'texto' : forms.Textarea(attrs={'class':'form-control'}),
            'activo' : forms.TextInput(attrs={'class':'form-control'}),
            'categoria' : forms.Select(attrs={'class':'form-control'}),
            'imagen' : forms.TextInput(attrs={'class':'form-control'}),
            'publicado' : forms.DateTimeInput(attrs={'class':'form-control'}),
            'autor' : forms.TextInput(attrs={'class':'form-control'}),
        }

class FormComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['comentario']
        widgets = {
            'comentario' : forms.Textarea(attrs={'class':'form-control'}),         
        #     'autor': forms.HiddenInput(attrs={'value':'user.id'}),
        #     'post': forms.HiddenInput(attrs={'value':'noticia.id'}),
        }

class ComentarioForm(forms.ModelForm):

    def init(self, args, **kwargs):
        super().init(args, **kwargs)
        self.fields['comentario'].widget.attrs.update({'rows': '3'})

    class Meta:
        model = Comentario
        fields = ['comentario']
        exclude = ['noticia']