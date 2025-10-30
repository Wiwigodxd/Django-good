from django.db import models
from django.core.validators import RegexValidator

class Producto(models.Model):
    # Se agregó esta nueva fila como clave primaria para los productos que se van agregando - Clave autoincrementable
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=32)
    precio = models.DecimalField(max_digits=999, decimal_places=2)
    descripcion = models.CharField(max_length=256, default="")
    cantidad = models.IntegerField(default=0)


class Ventas(models.Model):
    rut= models.CharField(max_length=10)
    cantidad = models.IntegerField(default=0)


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Ventas, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en {self.venta}"
    
class Cliente(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=32)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(
        max_length=9,
        validators=[RegexValidator(regex=r'^\d{1,9}$', message='El teléfono debe contener solo dígitos (máx. 9).')]
    )
# ...existing code...
class Formulario(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=32)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(
        max_length=9,
        validators=[RegexValidator(regex=r'^\d{1,9}$', message='El teléfono debe contener solo dígitos (máx. 9).')]
    )

