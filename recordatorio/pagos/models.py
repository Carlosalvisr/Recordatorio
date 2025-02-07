
from django.db import models

class Pago(models.Model):
    nombre = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_de_pago = models.DateField()
    frecuencia = models.CharField(max_length=50)  # Mensual, Anual, etc.

    def __str__(self):
     return self.nombre
