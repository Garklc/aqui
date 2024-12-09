from django.contrib import admin
from .models import VehiculoModel

@admin.register(VehiculoModel)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio')
    search_fields = ('marca', 'modelo', 'serial_carroceria', 'serial_motor')
