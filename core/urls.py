from .views import *
from django.urls import path
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', home, name="home"),
    path('accesorios', accesorios, name="accesorios"),
    path('productos', productos, name="productos"),
    path('carritos', carritos, name="carritos"),
    path('celulares', celulares, name="celulares"),
    path('computadores', computadores, name="computadores"),
    path('login', LoginView.as_view(Template_name='core/iniciarsesion.html'), name="login"),
    path('quienessomos', quienessomos, name="quienessomos"),
    path('registro', registro, name="registro"),
    path('addToCar/<id>', addToCar, name="addToCar"),
]
