from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


from .forms import FormularioRegistroUsuario, FormularioRegistroProveedor
from .models import Proveedor

def autenticar_usuario(request, usuario, contrasena):
    user = authenticate(request, username=usuario, password=contrasena)
    if user: login(request, user)
    return True if user is not None else False

def index(request):
    if request.method == 'POST':
        messages.success(request, "¡Has iniciado sesión!") if autenticar_usuario(request, request.POST['usuario'], request.POST['contrasena']) else messages.error(request, "¡Error al iniciar sesión!")
        return redirect('index')
    return render(request, 'index.html')

def cerrar_sesion(request):
    logout(request)
    messages.success(request, "¡Has cerrado sesión!")
    return redirect('index')

@login_required()
def lista_usuarios(request):
    "Vista para renderizar la página donde se mostrarán los datos de usuarios"
    usuarios = User.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

def registrar_usuario(request):
    if request.method == 'POST':
        form = FormularioRegistroUsuario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form = FormularioRegistroUsuario()
    return render(request, 'registro_usuario.html', {'form':form})

@login_required()
def registrar_proveedor(request):
    if request.method == 'POST':
        form = FormularioRegistroProveedor(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'proveedor.html', {'form': FormularioRegistroProveedor(), 'message': 'Proveedor guardado en la base de datos'})
    else:
        form = FormularioRegistroProveedor()
    
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor.html', {'form': form, 'proveedores': proveedores})