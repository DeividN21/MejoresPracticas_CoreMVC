from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from heladeria.models import Proveedor, CategoriaProv
from heladeria.views.proveedorBuilder import ProveedorBuilder

@login_required
def consultarP(request):
    proveedores = Proveedor.objects.all()
    categorias = CategoriaProv.objects.all()
    return render(request,"proveedores.html",{'proveedores' : proveedores,'categorias' : categorias})

def guardarP(request):
    if request.method == 'POST':
        # Usar el Builder para crear el objeto Proveedor
        proveedor = (ProveedorBuilder()
                    .set_nombre(request.POST["nombreProveedor"])
                    .set_categoria(request.POST["categoria"])
                    .set_costo_insumo(request.POST["costoInsumo"])
                    .set_tiempo_entrega(request.POST["tiempoEntrega"])
                    .build())

        proveedor.save()  # Guardar el proveedor en la base de datos
        messages.success(request, 'Proveedor agregado!')
        return redirect('consultarP')

def eliminarP(request, id):
    proveedor = Proveedor.objects.filter(pk=id)
    proveedor.delete()
    messages.success(request, 'Proveedor eliminado!')
    return redirect('consultarP')

def detalleP(request, id):
    proveedor = Proveedor.objects.get(pk=id)
    categorias = CategoriaProv.objects.all()
    return render(request, "proveedorEditar.html", {'proveedor' : proveedor, 'categorias' : categorias})

def editarP(request):
    nombreProveedor = request.POST["nombreProveedor"]
    categoria_id = request.POST["categoria"]
    costoInsumo = request.POST["costoInsumo"]
    tiempoEntrega = request.POST["tiempoEntrega"]
    categoriaProv = CategoriaProv.objects.get(pk=categoria_id)
    id = request.POST["id"]
    Proveedor.objects.filter(pk=id).update(id=id,nombreProveedor=nombreProveedor,categoriaProv=categoriaProv,
                                            costoInsumo=costoInsumo,tiempoEntrega=tiempoEntrega)
    messages.success(request, 'Proveedor actualizado con exito!')
    return redirect('consultarP')