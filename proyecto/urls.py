
from django.contrib import admin
from django.urls import path, include
from core.views import login_view  # Importa la vista de inicio de sesión


urlpatterns = [
    path('admin/login/', login_view, name='admin_login'),  
    path('admin/', admin.site.urls),
    path('', include('core.urls')), 
]
