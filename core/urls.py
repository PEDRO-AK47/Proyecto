from django.contrib import admin
from django.urls import path
from .views import *
from . import views
from core.views import *
from .views import logout_view


urlpatterns = [
    path('', home, name="home"),
    path('accesorios', accesorios, name="accesorios"),
    path('productos', productos, name="productos"),
    path('carrito', carrito, name="carrito"),
    path('celulares', celulares, name="celulares"),
    path('computadores', computadores, name="computadores"),
    path('login_user', login_user, name="login_user"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registro/', registro, name='registro'),
    path('quienessomos', quienessomos, name="quienessomos"),
    path('addtocar/<id_producto>/', addtocar, name="addtocar"),
    path('dropitem/<id_producto>/', dropitem, name="dropitem"),
    path('limpiar', limpiar),
    path('comprar', comprar, name="comprar")]
 