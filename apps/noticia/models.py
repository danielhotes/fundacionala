from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('home')

class Noticia(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='noticia', default='noticia/default.jpg')
    publicado = models.DateTimeField(default=timezone.now)
    autor = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo
    
    def delete(self, using = None, keep_parents = False):
        self.imagen.delete(self.imagen.name)
        super().delete()

    def get_absolute_url(self):
    #    #return reverse('detalle-noticia', kwargs={'pk': self.pk})
    #    #Si quisiese redireccionar a otra seccion ListView
        return reverse('home')
    

class Comentario(models.Model):
    post = models.ForeignKey(Noticia, related_name='comentarios', on_delete=models.CASCADE, auto_created=True)
    autor = models.ForeignKey(User, related_name='autor', on_delete=models.CASCADE, auto_created=True)
    comentario = models.TextField(null=False)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.titulo} - {self.autor} - {self.comentario}'