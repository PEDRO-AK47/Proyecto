from django.shortcuts import render,redirect

from .models import  Producto

def productos(request):
    productos = Producto.objects.all()
    context={"productos":productos}
    return render (request,'productos.html',context)

def login(request):
    return render(request, 'login.html')


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
def iniciarsesion(request):
    context={}
    return render(request, 'iniciarsesion.html', context)
def quienessomos(request):
    context={}
    return render(request, 'quienessomos.html', context)
def registro(request):
    context={}
    return render(request, 'registro.html', context)

def addToCar(request, id):
    carrito = request.session.get("carrito", [])
    producto = Producto.objets.get(id=id)
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
    

