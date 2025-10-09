from django.contrib import admin
from .models import Producto, Ventas, DetalleVenta, Cliente , Formulario
# Register your models here.

admin.site.register(Producto)
admin.site.register(Ventas)
admin.site.register(DetalleVenta)
admin.site.register(Cliente)
admin.site.register(Formulario)

