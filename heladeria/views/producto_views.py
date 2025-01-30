from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from heladeria.models import Producto, CategoriaPr

# Clase base para guardar productos
class ProductoGuardarHandler:
    def guardar(self, producto):
        producto.save()
        return producto

# Clase extendida para agregar notificaciones al guardar
class ProductoGuardarConNotificacion(ProductoGuardarHandler):
    def __init__(self, request):
        self.request = request  # Almacenar el objeto request

    def guardar(self, producto):
        super().guardar(producto)  # Llamar al método de la clase base
        messages.success(self.request, 'Producto agregado!')  # Usar self.request para mostrar el mensaje
        return producto

@login_required
def consultar(request):
    productos = Producto.objects.all()
    categorias = CategoriaPr.objects.all()
    return render(request,"productos.html",{'productos' : productos, 'categorias': categorias})

def guardar(request):
    if request.method == 'POST':
        nombre = request.POST["nombre"]
        precio = request.POST["precio"]
        costo = request.POST["costo"]
        cantidad = request.POST["cantidad"]
        categoria_id = request.POST["categoria"]
        categoriaPr = CategoriaPr.objects.get(pk=categoria_id)
        descripcion = request.POST["descripcion"]
        p = Producto(nombre=nombre, precio=precio, costo=costo, cantidad=cantidad, categoriaPr=categoriaPr, descripcion=descripcion)

        # Usar el handler para guardar el producto
        handler = ProductoGuardarConNotificacion(request)  # Instanciar el handler
        handler.guardar(p)  # Guardar el producto con notificación

        return redirect('consultar')

def eliminar(request, id):
    producto = Producto.objects.filter(pk=id)
    producto.delete()
    messages.success(request, 'Producto eliminado!')
    return redirect('consultar')

def detalle(request, id):
    producto = Producto.objects.get(pk=id)
    categorias = CategoriaPr.objects.all()
    return render(request, "productoEditar.html", {'producto' : producto, 'categorias': categorias})
    
def editar(request):
    nombre = request.POST["nombre"]
    precio = request.POST["precio"]
    costo = request.POST["costo"]
    cantidad = request.POST["cantidad"]
    categoria_id = request.POST["categoria"]
    descripcion = request.POST["descripcion"]
    categoriaPr = CategoriaPr.objects.get(pk=categoria_id)
    id = request.POST["id"]
    Producto.objects.filter(pk=id).update(id=id,nombre=nombre,precio=precio,costo=costo,cantidad=cantidad,categoriaPr=categoriaPr,descripcion=descripcion)
    messages.success(request, 'Producto actualizado con exito!')
    return redirect('consultar')