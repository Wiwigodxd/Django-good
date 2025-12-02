from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from inventario.views_dashboard import dashboard_data


router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"productos", views.ProductoViewSet)
router.register(r"ventas", views.VentasViewSet)
router.register(r"detalleventas", views.DetalleVentaViewSet)
router.register(r"clientes", views.ClienteViewSet)
router.register(r"formularios", views.FormularioViewSet)

urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

   
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),

 
    path("", views.lista_productos, name="lista_productos"),
    path("producto/<int:id>/", views.detalle_producto, name="detalle_producto"),
    path("producto/nuevo/", views.nuevo_producto, name="nuevo_producto"),
    path("producto/editar/<int:id>/", views.editar_producto, name="editar_producto"),
    path("producto/eliminar/<int:id>/", views.eliminar_producto, name="eliminar_producto"),
    path("producto/venta/<int:id>/", views.venta_producto, name="venta_producto"),
    path("ventas/", views.lista_ventas, name="lista_ventas"),
    path("cliente/", views.nuevo_cliente, name="nuevo_cliente"),
    path("cliente/", views.lista_cliente, name="lista_cliente"),
    path("cliente/nuevo/", views.formulario_cliente, name="formulario_cliente"),
    path("api/whoami/", views.whoami, name="whoami"),
    path("api/dashboard/", dashboard_data),

]
