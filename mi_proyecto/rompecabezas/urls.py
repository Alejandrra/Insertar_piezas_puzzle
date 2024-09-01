from django.urls import path
from . import views

urlpatterns = [
    path('cargar/', views.cargar_pieza, name='cargar_pieza'),
    path('piezas/', views.mostrar_piezas, name='mostrar_piezas'),
]
