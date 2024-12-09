from django.db import models
from django.contrib.auth.models import Permission

class VehiculoModel(models.Model):
    MARCAS = [
        ('FIAT', 'Fiat'),
        ('CHEVROLET', 'Chevrolet'),
        ('FORD', 'Ford'),
        ('TOYOTA', 'Toyota'),
    ]
    CATEGORIAS = [
        ('PARTICULAR', 'Particular'),
        ('TRANSPORTE', 'Transporte'),
        ('CARGA', 'Carga'),
    ]

    marca = models.CharField(max_length=20, choices=MARCAS, default='FORD')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='PARTICULAR')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.marca} {self.modelo}"

    class Meta:
        permissions = [
            ("visualizar_catalogo", "Can view vehicle catalog"),
        ]
