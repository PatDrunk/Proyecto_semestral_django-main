from django.forms import ModelForm
from .models import *

#creamos un template
class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = ['codigo', 'nombre','marca','precio','stock','tipo','imagen']


class ClienteForm(ModelForm):

    class Meta:
        model = Cliente
        fields = ['codigo','nombre','numero_telefono','direccion','correo','pais','imagen','tipo_cliente']