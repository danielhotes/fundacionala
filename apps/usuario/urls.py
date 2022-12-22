from django.urls import path
from .views import *

urlpatterns = [
    path('contacto', contacto, name='contacto'),
    path('registro/', registro, name='registro'),
    path('consultas/', ContactosView.as_view(), name='consultas'),
]
