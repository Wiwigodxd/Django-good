from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"productos", views.ProductoViewSet)
router.register(r"ventas", views.VentasViewSet)
router.register(r"detalleventas", views.DetalleVentaViewSet)
router.register(r"clientes", views.ClienteViewSet)
router.register(r"formularios", views.FormularioViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", views.lista_productos, name="lista_productos"),
    path("formulario", views.formulario_cliente, name="formulario_cliente"),
    path("ventas/", views.lista_ventas, name="lista_ventas"),
    path("cliente/", views.nuevo_cliente, name="nuevo_cliente"),
    path("cliente/", views.lista_cliente, name="lista_cliente"),
    path("producto/venta/<int:id>/", views.venta_producto, name="venta_producto"),
    path("producto/<int:id>/", views.detalle_producto, name="detalle_producto"),
    path("producto/nuevo/", views.nuevo_producto, name="nuevo_producto"),
    path("producto/editar/<int:id>/", views.editar_producto, name="editar_producto"),
    path("producto/eliminar/<int:id>/", views.eliminar_producto, name="eliminar_producto"),
]
