from django.shortcuts import render, redirect
from .models import Producto, Fabrica 

from .forms import ProductoFormAdd
from django.contrib import messages
from django.utils import timezone
from django.db import connection


# Create your views here.
   
           
def listado_productos_view(request):
    contexto = {}
    productos = Producto.objects.all()
    
    contexto["productos"] = productos
     
    mapeo = {'nombre':'nombre', 'vencimiento':'f_vencimiento', 'precio':'precio'}
    datos = Producto.objects.raw('SELECT id, nombre FROM Productos', translations=mapeo )
    for dato in datos:
        print(f'El producto: %s se vence en: %s, con un precio de : $ %s'%(dato.nombre, dato.f_vencimiento, dato.precio,))


    mapeo = {'nombre':'nombre', 'precio':'precio'}
    datos = Producto.objects.raw('SELECT id, nombre FROM Productos WHERE precio<=2500', translations=mapeo )
    for dato in datos:
        print(f'El producto: %s tiene un precio de : $ %s'%(dato.nombre, dato.precio,))
   
    nombre = 'P&G'
    cursor = connection.cursor()
    cursor.execute("UPDATE fabricas SET pais = 'Canada' WHERE nombre = %s", [nombre])
    cursor.execute("SELECT pais from fabricas WHERE nombre = %s", [nombre])
    row = cursor.fetchall()
    print(row)
    
    return render(request, "inventario/listado_productos.html", contexto)
    
def add_producto(request):
    contexto = {}
        
    if request.method == 'GET':
        contexto["form"] = ProductoFormAdd()
        return render(request, 'inventario/add_producto.html', contexto)
    
    if request.method == 'POST':   #
        
        form = ProductoFormAdd(request.POST)
        contexto["form"] = form 
        
        print(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, "Producto creado correctamente.")
            return redirect('listado_productos')
            
        else:
            messages.error(request, "Algo ha fallado, revise bien los datos ingresados.")
            return render(request, 'inventario/add_producto.html', contexto)
  