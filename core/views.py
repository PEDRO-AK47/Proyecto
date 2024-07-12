from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import  Producto
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages
from .forms import *

def comprar(request):
    carrito = request.session.get("carrito",[])
    total = 0
    for item in carrito: 
        total += item[5]
    venta = venta()
    venta.cliente = request.User
    venta.total = total
    venta.save()
    for item in carrito:
        detalle = detalle()
        detalle.producto = Producto.objects.get(id_producto =item[0])
        detalle.precio = item[3]
        detalle.cantidad = item[4]
        detalle.venta = venta
        detalle.save()

    return redirect(to="carrito")


def carrito(request):
    return render(request, 'carritos.html', {"carrito":request.session.get("carrito",[])})


def productos(request):
    Producto = Producto.objects.all()
    context={"productos":productos}
    return render (request,'productos.html',context)

def home(request):
    celulares = Producto.objects.all()
    return render(request, 'blaze cats.html', {'celulares':celulares, "carrito":request.session.get("carrito",[])})

def celulares(request):
    context={}
    return render(request, 'celulares.html', context)
def accesorios(request):
    context={}
    return render(request, 'accesorios.html', context)

def computadores(request):
    context={}
    return render(request, 'computadores.html', context)
def quienessomos(request):
    context={}
    return render(request, 'quienessomos.html', context)
def registro(request):
    if request.method == "POST":
        registro = Registro(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to="login_view")
        else:
            registro = Registro()
    return render(request, 'Registro.html', {'form':registro})
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


def dropitem(request, id_producto):
    carrito = request.session.get("carrito", [])
    for item in carrito:
        if item[0] == id_producto:
            if item[4] > 1:

                item[4] -= 1
                item[5] = item[3] * item[4]
                break
            else:
                carrito.remove(item)
    request.session["carrito"] = carrito    
    return redirect(to="carrito")




def addtocar(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    carrito = request.session.get("carrito", [])
    for item in carrito:
        if item[0] == id_producto:
            item[4] += 1
            item[5] = item[3] * item[4]
            break
    else:            
        carrito.append([id_producto,producto.info, producto.imagen, producto.precio,1,producto.precio])
    request.session["carrito"] = carrito    
    return redirect(to="home")

def limpiar(request):
    request.session.flush()
    return redirect(to="home")

    

