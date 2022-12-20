from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Noticia, Categoria, Comentario
from .forms import NoticeForm, FormComentario, ComentarioForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User

# Create your views here.

class HomeView(ListView):
    model = Noticia
    template_name = 'home.html'

class NoticeDetailView(DetailView):
    model = Noticia
    template_name = 'noticia/detallenoticias.html'

class NoticiaView(ListView):
    model = Noticia
    template_name = 'noticia/listadonoticias.html'

#@permission_required('noticia.add_noticia')
class CrearNoticiaView(CreateView):
    model = Noticia
    template_name = 'noticia/agregarnoticia.html'
    fields = '__all__'

# def agregar_noticia(request):
#     data = {
#         'form': AgregarNoticiaForm()
#     }

#     if request.method == 'POST':
#         formulario = AgregarNoticiaForm(data=request.POST, files=request.FILES)
#         if formulario.is_valid():
#             formulario.save()
#             data['mensaje'] = 'Noticia creada!'
#         else:
#             data['form'] = formulario
#     return render(request, 'agregarnoticia.html', data)

#@permission_required('noticia.change_noticia')
class EditNoticeView(UpdateView):
    model = Noticia
    form_class = NoticeForm
    template_name = 'noticia/editarnoticia.html'

#@permission_required('noticia.delete_noticia')
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

class DeleteCategoriaView(DeleteView):
    model = Categoria
    template_name = 'categoria/borrar_categoria.html'
    success_url = reverse_lazy('noticias')

def CategoriaView(request, cats):
    cats_noticia = Noticia.objects.filter(categoria=cats)
    return render(request, 'categoria/categorias.html', {'cats':cats, 'cats_noticia':cats_noticia})

class CrearComentarioView(CreateView):
    model = Comentario
    form_class = FormComentario
    template_name = 'noticia/agregar_comentario.html'
    #fields = '__all__'
    def form_valid(self, form):
        form.instance.autor_id = self.request.user.id
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('noticias')

# def Comentar(request):
#     comentarios = Comentario.objects.all()
#     usuario = request.user.id

#     context={
#         'comentarios' : comentarios,
#         'usuario': usuario,
#     }
#     return render(request,'comentario/listadoComentario.html', context)


# def agregarComentario(request):
#     usuario = User.id
#     form = ComentarioForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ComentarioForm()

#     context={
#         'form': form,
#         'usuario': usuario,
#     }
#     return render(request,'noticia/agregar_comentario.html', context)