from django.contrib import admin
from .models import *
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre','marca','precio','stock','tipo','imagen']
    search_fields = ["codigo"]
    list_per_page = 3

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre','numero_telefono','direccion','correo','pais','imagen','tipo_cliente']
    search_fields = ["codigo"]
    list_per_page = 3


admin.site.register(TipoProducto)
admin.site.register(Producto)
admin.site.register(TipoCliente)
admin.site.register(Cliente)
admin.site.register(Carrito)