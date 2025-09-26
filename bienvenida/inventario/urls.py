from django.urls import path
from . import views
urlpatterns = [
    path("", views.lista_productos, name="lista_productos"),
    path("ventas/", views.lista_ventas, name="lista_ventas"),
    path("cliente/", views.nuevo_cliente, name="nuevo_cliente"),
    path("cliente/", views.lista_cliente, name="lista_cliente"),
    path("producto/venta/<int:id>/", views.venta_producto, name="venta_producto"),
    path("producto/<int:id>/", views.detalle_producto, name="detalle_producto"),
    path("producto/nuevo/", views.nuevo_producto, name="nuevo_producto"),
    path("producto/editar/<int:id>/", views.editar_producto, name="editar_producto"),
    path("producto/eliminar/<int:id>/", views.eliminar_producto, name="eliminar_producto"),
]