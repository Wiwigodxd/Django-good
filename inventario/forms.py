from django import forms
from .models import Producto
from .models import Ventas
from .models import Cliente
from .models import Formulario


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto 
        fields = ['nombre', 'precio', 'descripcion', 'cantidad']

class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = ['rut','cantidad']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut','nombre','correo','telefono']

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ['rut','nombre','correo','telefono']
