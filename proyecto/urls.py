
from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),
path('celulares', celulares, name="celulares"),

]
