from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import  Producto
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages



def productos(request):
    productos = Producto.objects.all()
    context={"productos":productos}
    return render (request,'productos.html',context)

def home(request):
    context={}
    return render(request, 'blaze cats.html', context)

def celulares(request):
    context={}
    return render(request, 'celulares.html', context)
def accesorios(request):
    context={}
    return render(request, 'accesorios.html', context)

def carritos(request):
    context={}
    return render(request, 'carritos.html', context)
def computadores(request):
    context={}
    return render(request, 'computadores.html', context)
def quienessomos(request):
    context={}
    return render(request, 'quienessomos.html', context)
def registro(request):
    context={}
    return render(request, 'Registro.html', context)
def login_user(request):
    context={}
    return render(request, 'login.html',context )

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_superuser:
                return redirect('home')
            else:
                return redirect('home')
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('home')
                else:
                    return redirect('home')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'iniciarsesion.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('home')

def addToCar(request, id):
    carrito = request.session.get("carrito", [])
    producto = Producto.objects.get(id=id)
    for item in carrito:
        if item["id"] == id:
            item["cantidad"] += 1
            item["subtotal"] = item["cantidad"] * item["precio"]
            break
    else:
            
        carrito.append({"id":id, "nombre" :producto.nombre, "imagen":producto.imagen,
        "precio":producto.precio, "cantidad":1, "subtotal":producto.precio})
    print(carrito)
    request.session["carrito"] = carrito
    request.session.flush()
    return redirect(to= "home")
    

