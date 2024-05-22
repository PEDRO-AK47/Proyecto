from django.shortcuts import render

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
    

