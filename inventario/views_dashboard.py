from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Count, Sum
from django.contrib.auth.models import User

from .models import InicioSesion, DetalleVenta

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_data(request):

    # 1️⃣ Cantidad de inicios de sesión
    sesiones = (
        InicioSesion.objects.values("usuario__username")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    # 2️⃣ Productos más y menos vendidos
    productos = (
        DetalleVenta.objects.values("producto__nombre")
        .annotate(total_vendido=Sum("cantidad"))
        .order_by("-total_vendido")
    )

    # 3️⃣ Detalle de ventas
    detalles = [
        {
            "producto": d.producto.nombre,
            "descripcion": d.producto.descripcion,
            "precio": float(d.producto.precio),
            "cantidad": d.cantidad,
        }
        for d in DetalleVenta.objects.select_related("producto").all()
    ]

    return Response({
        "sesiones": list(sesiones),
        "productos": list(productos),
        "detalles": detalles,
    })
