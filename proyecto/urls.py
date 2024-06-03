
from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),
    path('celulares', celulares, name="celulares"),
    path('carritos', carritos, name="carritos"),
    path('computadores', computadores, name="computadores"),
    path('iniciarsesion', iniciarsesion, name="iniciarsesion"),
    path('quienessomos', quienessomos, name="quienessomos"),
    path('registro', registro, name="registro"),
    path('accesorios', accesorios, name="accesorios"),

]
