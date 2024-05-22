from .views import *
from django.urls import path


urlpatterns = [
    path('', home, name="home"),
    path('', accesorios, name="accesorios"),
    path('', carritos, name="carritos"),
    path('celulares', celulares, name="celulares"),
    path('', computadores, name="computadores"),
    path('', iniciarsesion, name="iniciarsesion"),
    path('', quienessomos, name="quienessomos"),
    path('', registro, name="registro"),
]
