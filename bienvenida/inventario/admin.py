from django.contrib import admin
from .models import Producto, Ventas, DetalleVenta
# Register your models here.

admin.site.register(Producto)
admin.site.register(Ventas)
admin.site.register(DetalleVenta)

