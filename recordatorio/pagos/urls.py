from django.urls import path
from .views import lista_pagos, agregar_pago, editar_pago

urlpatterns = [
    path('', lista_pagos, name='lista_pagos'),
    path('agregar/', agregar_pago, name='agregar_pago'),
    path('editar/<int:pk>/', editar_pago, name='editar_pago'),
]