from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Noticia, Categoria, Comentario
from .forms import FormComentario
from django.urls import reverse_lazy

# Create your views here.

class HomeView(ListView):
    model = Noticia
    template_name = 'home.html'

class NoticeDetailView(DetailView):
    model = Noticia
    template_name = 'noticia/detallenoticias.html'

def detalle_noticia(request,pk):
    noticia_detail = Noticia.objects.filter(id=pk)
    noticia = Noticia.objects.all()
    lista_cats = Categoria.objects.all()
    ctx = {
        'noticia_detail':noticia_detail,
        'noticia':noticia,
        'lista_cats':lista_cats
    }
    return render(request, 'noticia/detallenoticias.html', ctx)

class NoticiaView(ListView):
    model = Noticia
    template_name = 'noticia/listadonoticias.html'

def listar_noticias(request):    
    noticia = Noticia.objects.all()
    lista_cats = Categoria.objects.all()
    ctx = {
        'noticia':noticia,
        'lista_cats':lista_cats
    }
    return render(request, 'noticia/listadonoticias.html', ctx)

class CrearNoticiaView(CreateView):
    model = Noticia
    template_name = 'noticia/agregarnoticia.html'
    fields = '__all__'

class EditNoticeView(UpdateView):
    model = Noticia
    template_name = 'noticia/editarnoticia.html'
    fields = '__all__'

class DeleteNoticeView(DeleteView):
    model = Noticia
    template_name = 'noticia/borrarnoticia.html'
    success_url = reverse_lazy('noticias')

class CrearCategoriaView(CreateView):
    model = Categoria
    template_name = 'categoria/agregar_categoria.html'
    fields = '__all__'

class EditCategoriaView(UpdateView):
    model = Categoria
    template_name = 'categoria/editar_categoria.html'
    fields = '__all__'

class DeleteCategoriaView(DeleteView):
    model = Categoria
    template_name = 'categoria/borrar_categoria.html'
    success_url = reverse_lazy('listado_categorias')

def CategoriaView(request, cats):
    cats_noticia = Noticia.objects.filter(categoria=cats)
    return render(request, 'categoria/categorias.html', {'cats':cats, 'cats_noticia':cats_noticia})

class CrearComentarioView(CreateView):
    model = Comentario
    form_class = FormComentario
    template_name = 'noticia/agregar_comentario.html'
    def form_valid(self, form):
        form.instance.autor_id = self.request.user.id
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('noticias')

class ListCatsView(ListView):
    model = Categoria
    template_name = 'categoria/lista_categorias.html'