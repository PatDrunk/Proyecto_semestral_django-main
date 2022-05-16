from django.shortcuts import *
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request,'app/index.html')

def base(request):
    return render(request,'app/base.html')

def login(request):
    return render(request,'app/index_login.html')

def carrito(request):
    return render(request, 'app/carrito_compra.html')

def historial(request):
    return render(request, 'app/historial.html')

def listaproducto(request):
    return render(request, 'app/lista_producto.html')

def perfil(request):
    return render(request, 'app/perfil.html')

def seguimiento(request):
    return render(request, 'app/seguimiento.html')

def listarProductos(request):
    productosAll = Producto.objects.all()
    datos ={ 'listaProductos' : productosAll}

    if request.method == 'POST':
        carrito = Carrito()
        carrito.nombre = request.POST.get('nombre')
        carrito.precio = request.POST.get('precio')
        carrito.imagen = request.POST.get('imagen')
        carrito.save()

    return render(request, 'app/productos/listarProductos.html',datos)

def agregarProductos(request):
    datos = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Producto guardado correctamente!'

    return render(request, 'app/productos/agregarProductos.html',datos)

def modificarProductos(request,codigo):
    producto = Producto.objects.get(codigo=codigo)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto modificado correctamente"
            datos['form'] = formulario
            
    return render(request, 'app/productos/modificarProductos.html',datos)

def eliminarProductos(request,codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect(to="listarProductos")

def listarClientes(request):
    clientesAll = Cliente.objects.all()
    datos ={
        'listaClientes' : clientesAll
    }
    return render(request, 'app/clientes/listarClientes.html',datos)

def agregarClientes(request):
    datos = {
        'formc' : ClienteForm()
    }
    if request.method == 'POST':
        formulario = ClienteForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Cliente guardado correctamente!'

    return render(request, 'app/clientes/agregarClientes.html',datos)

def modificarClientes(request,codigo):
    Cliente = Cliente.objects.get(codigo=codigo)
    datos = {
        'form' : ClienteForm(instance=Cliente)
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, files=request.FILES, instance=Cliente)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Cliente modificado correctamente"
            datos['form'] = formulario
            
    return render(request, 'app/clientes/modificarClientes.html',datos)

def eliminarClientes(request,codigo):
    cliente = Cliente.objects.get(codigo=codigo)
    cliente.delete()

    return redirect(to="listarClientes")

def carritoCompras(request):
    carrito = Carrito.objects.all()
    datos = { 'listaCarrito' : carrito}

    return render(request, 'app/productos/carritoCompras.html',datos)

def compraExitosa(request):
    carrito = Carrito.objects.all()
    carrito.delete

    return render(request, 'app/productos/compraExitosa.html')
