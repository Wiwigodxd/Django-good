from django.db import models


class Producto(models.Model):
    # Se agregó esta nueva fila como clave primaria para los productos que se van agregando - Clave autoincrementable
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=32)
    precio = models.DecimalField(max_digits=999, decimal_places=2)
    descripcion = models.CharField(max_length=256, default="")
    cantidad = models.IntegerField(default=0)


class Ventas(models.Model):
    rut= models.CharField(max_length=13)
    cantidad = models.IntegerField(default=0)


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Ventas, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en {self.venta}"
