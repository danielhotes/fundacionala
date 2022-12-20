from django.urls import path
from .views import *

urlpatterns = [
    #path('registro/', RegistroUsuarioView.as_view(), name='registro'),
    path('contacto', contacto, name='contacto'),
    path('registro/', registro, name='registro'),
]
