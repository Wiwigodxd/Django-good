from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .models import Ventas, DetalleVenta
from .forms import ProductoForm
from .forms import VentasForm


def lista_ventas(request):
    ventas = DetalleVenta.objects.all()
    return render(request, 'inventario/ventas.html', {'ventas': ventas})


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