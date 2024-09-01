from django.shortcuts import render, redirect
from .forms import PiezaForm
from .models import Pieza

def cargar_pieza(request):
    if request.method == 'POST':
        form = PiezaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mostrar_piezas')
    else:
        form = PiezaForm()
    return render(request, 'rompecabezas/cargar_pieza.html', {'form': form})

def mostrar_piezas(request):
    piezas = Pieza.objects.all()
    return render(request, 'rompecabezas/mostrar_piezas.html', {'piezas': piezas})

