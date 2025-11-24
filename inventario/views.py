from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Formulario, Cliente, Ventas, DetalleVenta
from .forms import ProductoForm, VentasForm, ClienteForm, FormularioForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .serializers import (
    GroupSerializer, UserSerializer, ProductoSerializer, 
    VentasSerializer, DetalleVentaSerializer, ClienteSerializer, 
    FormularioSerializer
)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def whoami(request):
    return Response({
        "username": request.user.username,
        "is_staff": request.user.is_staff,
        "is_superuser": request.user.is_superuser,
    })


# ===========================================================
# DECORADOR: SOLO SUPERUSUARIO (y debe estar logueado)
# ===========================================================
def superuser_required(view_func):
    decorated_view = login_required(
        user_passes_test(lambda u: u.is_superuser)(view_func)
    )
    return decorated_view


# ===========================================================
# API REST (requiere token y login)
# ===========================================================
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by("nombre")
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]

class VentasViewSet(viewsets.ModelViewSet):
    queryset = Ventas.objects.all().order_by("rut")
    serializer_class = VentasSerializer
    permission_classes = [permissions.IsAuthenticated]

class DetalleVentaViewSet(viewsets.ModelViewSet):
    queryset = DetalleVenta.objects.all().order_by("venta")
    serializer_class = DetalleVentaSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by("nombre")
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]

class FormularioViewSet(viewsets.ModelViewSet):
    queryset = Formulario.objects.all().order_by("nombre")
    serializer_class = FormularioSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# ===========================================================
# VISTAS HTML – SOLO SUPERUSUARIO
# ===========================================================

@superuser_required
def formulario_cliente(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cliente')
    else:
        form = FormularioForm()
    return render(request, 'inventario/formulario.html', {'formulario': form})


@superuser_required
def nuevo_cliente(request):
    cliente = Formulario.objects.all()
    return render(request, 'inventario/cliente.html', {'cliente': cliente})


@superuser_required
def lista_cliente(request):
    cliente = Cliente.objects.all()
    return render(request, 'inventario/lista_cliente.html', {'cliente': cliente})


@superuser_required
def lista_ventas(request):
    ventas = DetalleVenta.objects.all()
    return render(request, 'inventario/ventas.html', {'ventas': ventas})


@superuser_required
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'inventario/lista_productos.html', {'productos': productos})


@superuser_required
def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'inventario/detalle_producto.html', {'producto': producto})


@superuser_required
def nuevo_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'inventario/nuevo_producto.html', {'form': form})


@superuser_required
def venta_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        ventas_form = VentasForm(request.POST)
        if ventas_form.is_valid():
            venta = ventas_form.save()

            DetalleVenta.objects.create(
                venta=venta,
                producto=producto,
                cantidad=venta.cantidad
            )

            producto.cantidad -= venta.cantidad
            producto.save()

            return redirect('lista_ventas')
    else:
        ventas_form = VentasForm()

    return render(request, 'inventario/vender_producto.html', {
        'ventas_form': ventas_form,
        'producto': producto
    })


@superuser_required
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'inventario/editar_producto.html', {'form': form})


@superuser_required
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'inventario/eliminar_producto.html', {'producto': producto})
