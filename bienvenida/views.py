from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto
from rest_framework import permissions
def lista_productos(request):
 productos = Producto.objects.all()
 return render(request, 'productos/lista.html', {'productos': productos})

def inicio(request):
     return HttpResponse("Hola causas que lo que 👻🤑")

