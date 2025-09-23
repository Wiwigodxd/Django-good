from django import forms
from .models import Producto
from .models import Ventas

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto 
        fields = ['nombre', 'precio', 'descripcion', 'cantidad']

class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = ['rut','cantidad']
        label = {"rut":"rut cliente"}
