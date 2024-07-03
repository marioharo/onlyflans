from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Flan, ContactForm, NewsletterForm # form del front
from .forms import ContactFormForm # form del back

# Create your views here.


def login(request):
    """vista necesaria para el logeo exitoso y redireccionamiento a la vista con autentificación"""
    return redirect('accounts/login')


def home(request):
    """Utiliza el template home.html"""
    # formulario newsletter
    if request.method == "POST":
        newsletter_email = request.POST['newsletter_email']
        NewsletterForm.objects.create(
            newsletter_email = newsletter_email,
        )
        return redirect('../exito/')
    else:
        #flanes = Flan.objects.all() # muestra todos los productos
        flanes = Flan.objects.filter(is_private = False) # filtra los productos por no privado
        return render(request, 'home.html', context={'flanes':flanes})


def acerca(request):
    """Utiliza el template acerca.html"""
    return render(request, 'acerca.html', context={})


@login_required
def bienvenido(request):
    """Utiliza el template bienvenido.html"""
    flanes = Flan.objects.filter(is_private = True) # filtra los productos por privado
    return render(request, 'bienvenido.html', context={"flanes":flanes})


# def contacto(request):
#     """Formulario que utiliza el template contacto.html con GET y envía los valores hacia la bbdd con POST"""
#     if request.method == "GET":
#         return render(request, 'contacto.html', context={})
#     else:
#         nombre = request.POST['Nombre']
#         apellido = request.POST['Apellido']
#         email = request.POST['Correo']
#         mensaje = request.POST['Mensaje']
#         ContactForm.objects.create(
#             nombre = nombre.title(),
#             apellido = apellido.title(),
#             email = email,
#             mensaje = mensaje,
#         )
#     return HttpResponse("Formulario recibido")

def contacto(request):
    """Formulario que utiliza el template contacto.html con GET y envía los valores hacia la bbdd con POST"""
    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            # proceso por el cual es registrado el contenido del formulario en el admin
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            # redirecciona a la nueva url
            return redirect('../exito/')
    else:
        form = ContactFormForm()
        
    return render(request, 'contacto.html', context={'form':form})


def exito(request):
    return render(request, 'exito.html', context={})