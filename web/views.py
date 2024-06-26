from django.shortcuts import render
from django.http import HttpResponse
from .models import Flan

# Create your views here.


def home(request):
    """Utiliza el template home.html"""
    flanes = Flan.objects.all()
    print(flanes)
    return render(request, 'home.html', context={'flanes':flanes})


def acerca(request):
    """Utiliza el template acerca.html"""
    return render(request, 'acerca.html', context={})


def bienvenido(request):
    """Utiliza el template bienvenido.html"""
    return render(request, 'bienvenido.html', context={})


def contacto(request):
    """Utiliza el template contacto.html"""
    return render(request, 'contacto.html', context={})


def enviar_formulario(request):
    return HttpResponse("""Formulario Recibido""")
