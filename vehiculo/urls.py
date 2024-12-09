from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_vehiculos, name='listar_vehiculos'),
    path('agregar/', views.agregar_vehiculo, name='agregar_vehiculo'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehiculo/', include('vehiculo.urls')),
]
