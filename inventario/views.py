from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .models import Formulario, Cliente, Ventas, DetalleVenta
from .forms import ProductoForm
from .forms import VentasForm
from .forms import ClienteForm
from .forms import FormularioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from serializers import GroupSerializer, UserSerializer, ProductoSerializer, VentasSerializer, DetalleVentaSerializer, ClienteSerializer, FormularioSerializer

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



def formulario_cliente(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cliente')
    else:
        form = FormularioForm()
    return render(request, 'inventario/formulario.html', {'formulario': form})


def nuevo_cliente(request):
    cliente = Formulario.objects.all()
    return render(request, 'inventario/cliente.html', {'cliente': cliente})


def lista_cliente(request):
    cliente = Cliente.objects.all()
    return render(request, 'inventario/lista_cliente.html', {'cliente': cliente})


def lista_ventas(request):
    ventas = DetalleVenta.objects.all()
    return render(request, 'inventario/ventas.html', {'ventas': ventas})


@login_required
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'inventario/lista_productos.html', {'productos': productos})


def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'inventario/detalle_producto.html', {'producto': producto})


def nuevo_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'inventario/nuevo_producto.html', {'form': form})


def venta_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        ventas_form = VentasForm(request.POST)
        if ventas_form.is_valid():
            venta = ventas_form.save()  # Guarda la venta

            # Crear detalle de la venta, relacionando con el producto actual
            DetalleVenta.objects.create(
                venta=venta,
                producto=producto,
                cantidad=venta.cantidad  # o puedes usar otra lógica si quieres más precisión
            )

            # Opcional: actualizar stock del producto
            producto.cantidad -= venta.cantidad
            producto.save()

            return redirect('lista_ventas')
    else:
        ventas_form = VentasForm()

    return render(request, 'inventario/vender_producto.html', {
        'ventas_form': ventas_form,
        'producto': producto
    })


def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    print(producto)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'inventario/editar_producto.html', {'form': form})


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'inventario/eliminar_producto.html', {'producto': producto})

