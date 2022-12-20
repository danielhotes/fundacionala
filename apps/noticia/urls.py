from django.urls import path
from .views import *

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('noticias/<int:pk>', NoticeDetailView.as_view(), name='detalle-noticia'),
    path('noticias', NoticiaView.as_view(), name='noticias'),
    #path('agregar_noticia', agregar_noticia, name='agregar_noticia'),
    path('agregar_noticia', CrearNoticiaView.as_view(), name='agregar_noticia'),
    path('agregar_categoria', CrearCategoriaView.as_view(), name='agregar_categoria'),
    path('noticias/editar/<int:pk>', EditNoticeView.as_view(), name='editar_noticia'),
    #path('categoria/editar/<int:pk>', EditCategoriaView.as_view(), name='editar_categoria'),
    path('noticias/<int:pk>/borrar', DeleteNoticeView.as_view(), name='borrar_noticia'),
    #path('categoria/<int:pk>/borrar', DeleteCategoriaView.as_view(), name='borrar_categoria'),
    path('categoria/<str:cats>/', CategoriaView, name='categoria'),
    path('noticias/<int:pk>/comentario/', CrearComentarioView.as_view(), name='comentario'),
    #path('noticias/comentario/', agregarComentario, name='comentario'),
]