from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Producto, Ventas, DetalleVenta, Cliente, Formulario

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ["url", "id", "nombre", "precio", "descripcion", "cantidad"]

class VentasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ventas
        fields = ["url", "rut", "cantidad"]

class DetalleVentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = ["url", "venta", "producto", "cantidad"]

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ["url", "rut", "nombre", "correo", "telefono"]

class FormularioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Formulario
        fields = ["url", "rut", "nombre", "correo", "telefono"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]

