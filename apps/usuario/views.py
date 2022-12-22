from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import FormContacto, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import Contacto

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            return redirect(to='home')
        else:
            data['form'] = formulario
    return render(request, 'registration/registracion.html', data)

def contacto(request):
    data = {
        'form': FormContacto()
    }
    if request.method == 'POST':
        formulario = FormContacto(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Consulta enviada!'
        else:
            data['form'] = formulario
    return render(request, 'contacto.html', data)

class ContactosView(ListView):
    model = Contacto
    template_name = 'consultas.html'