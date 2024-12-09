from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import VehiculoModel

@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def listar_vehiculos(request):
    vehiculos = VehiculoModel.objects.all()
    return render(request, 'vehiculo/listar.html', {'vehiculos': vehiculos})

@permission_required('vehiculo.add_vehiculomodel', raise_exception=True)
def agregar_vehiculo(request):
    # Aquí iría la lógica de creación del vehículo (por ejemplo, un formulario).
    return render(request, 'vehiculo/agregar.html')
