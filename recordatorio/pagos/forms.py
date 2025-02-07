from django import forms
from .models import Pago

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['nombre', 'monto', 'fecha_de_pago', 'frecuencia']