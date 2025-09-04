from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=32)
    precio = models.DecimalField(max_digits=999,decimal_places=2)
    descripcion= models.CharField(max_length=256, default="")
    stock = models.IntegerField(default=0)
