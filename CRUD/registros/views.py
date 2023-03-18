from django.shortcuts import render, redirect
from .models import Producto

# Create your views here.
def mostrar_todos_los_productos(request):
    showall = Producto.objects.all()
    return render(request, 'index.html', {'productos': showall})

def delete_product(request, id):
    delete = Producto.objects.get(id=id)
    delete.delete()
    return redirect("/registros/")

def create_product(request):
    new_descripcion = request.POST["descripcion"]
    new_categoria = request.POST["categoria"]
    new_precio = request.POST["precio"]
    new_cantidad = request.POST["cantidad"]
    new_categoria_descripcion = request.POST["categoriadesc"]

    if new_descripcion == "" or new_categoria == "" or new_precio == "" or new_cantidad == "" or new_categoria_descripcion == "":
        product = Producto.objects.all()
        return render(
            request, "index.html", {"Producto": Producto, "error": "Falta un dato requerido"}
        )
    product = Producto(descripcion=new_descripcion, categoria=new_categoria,precio=new_precio, cantidad=new_cantidad,categoriadesc=new_categoria_descripcion)
    product.save()
    return redirect("/registros/")


def update(request, id):
    actualizar = Producto.objects.get(id=id)
    return render(request, 'update.html', {'productos': actualizar})

def create_product(request):
    id = request.POST["id"]
    new_descripcion = request.POST["descripcion"]
    new_categoria = request.POST["categoria"]
    new_precio = request.POST["precio"]
    new_cantidad = request.POST["cantidad"]
    new_categoria_descripcion = request.POST["categoriadesc"]

    if new_descripcion == "" or new_categoria == "" or new_precio == "" or new_cantidad == "" or new_categoria_descripcion == "":
        product = Producto.objects.all()
        return render(
            request, "index.html", {"Producto": Producto, "error": "Falta un dato requerido"}
        )
    actualizar = Producto(id=id, descripcion=new_descripcion, categoria=new_categoria,precio=new_precio, cantidad=new_cantidad,categoriadesc=new_categoria_descripcion)
    actualizar.save()
    return redirect("/registros/")