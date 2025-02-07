from django.shortcuts import render, redirect, get_object_or_404
from .models import Pago
from .forms import PagoForm

def lista_pagos(request):
    pagos = Pago.objects.all()
    return render(request, 'pagos/lista_pagos.html', {'pagos': pagos})

def agregar_pago(request):
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pagos')
    else:
        form = PagoForm()
    return render(request, 'pagos/agregar_pago.html', {'form': form})

def editar_pago(request, pk):
    pago = get_object_or_404(Pago, pk=pk)
    if request.method == 'POST':
        form = PagoForm(request.POST, instance=pago)
        if form.is_valid():
            form.save()
            return redirect('lista_pagos')
    else:
        form = PagoForm(instance=pago)
    return render(request, 'pagos/editar_pago.html', {'form': form})