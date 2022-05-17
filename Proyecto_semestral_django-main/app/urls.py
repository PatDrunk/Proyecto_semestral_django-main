from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name = ''),
    path("base/", base, name='base'),
    path("index_login/", login, name='login'),
    path("historial/",historial, name='historial'),
    path("productos/",productos, name='productos'),
    path("seguimiento/", seguimiento, name='seguimiento'),

    path("agregarProductos/", agregarProductos, name='agregarProductos'),
    path("listarProductos/",listarProductos, name='listarProductos'),
    path("modificarProductos/<codigo>/",modificarProductos, name='modificarProductos'),
    path("eliminarProductos/<codigo>/",eliminarProductos, name='eliminarProductos'),

    path("agregarClientes/",agregarClientes, name='agregarClientes'),
    path("listarClientes/",listarClientes, name='listarClientes'),
    path("eliminarClientes/<codigo>/",eliminarClientes, name='eliminarClientes'),
    path("modificarClientes/<codigo>/",modificarClientes, name='modificarClientes'),

    path("carritoCompras/",carritoCompras, name='carritoCompras'),
    path("compraExitosa/",compraExitosa, name='compraExitosa'),
]