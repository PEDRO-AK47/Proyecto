from .views import *
from django.urls import path


urlpatterns = [
    path('', home, name="home"),
    path('accesorios', accesorios, name="accesorios"),
    path('productos', productos, name="productos"),
    path('carritos', carritos, name="carritos"),
    path('celulares', celulares, name="celulares"),
    path('computadores', computadores, name="computadores"),
    path('iniciarsesion', iniciarsesion, name="iniciarsesion"),
    path('quienessomos', quienessomos, name="quienessomos"),
    path('registro', registro, name="registro"),
    path('addToCar/<id>', addToCar, name="addToCar"),
]
