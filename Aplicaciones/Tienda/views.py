from django.shortcuts import render, redirect
from .models import Tienda
from django.contrib import messages 

# Create your views here.
def inicioTienda(request):
    listadoTienda = Tienda.objects.all()
    return render(request, "Tienda/inicioTienda.html", {'perros': listadoTienda})

def nuevaTienda(request):
    return render(request, "Tienda/nuevaTienda.html")

def guardarTienda(request):
    if request.method == "POST":
        id = request.POST.get('id')
        nombre = request.POST["nombre"]
        direccion = request.POST["direccion"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        fecha = request.POST['fecha']

        Tienda.objects.create(nombre=nombre, direccion=direccion, telefono=telefono, email=email, fecha = fecha)
        messages.success(request, "SE HA AGREGADO LA TIENDA")

        return redirect('indexTienda')
    return redirect('indexTienda')

def eliminarTienda(request, id):
    tiendaEliminar = Tienda.objects.get(id=id)
    tiendaEliminar.delete()
    messages.success(request, "SE HA ELIMINADO LA TIENDA")
    return redirect('indexTienda')

def editarTienda(request, id):
    tienda = Tienda.objects.get(id=id)
    return render(request, "Tienda/editarTienda.html", {'perro': tienda})

def procesarEdicionTienda(request, id):
    nombre = request.POST["nombre"]
    direccion = request.POST["direccion"]
    telefono = request.POST["telefono"]
    email = request.POST["email"]
    fecha = request.POST['fecha']

    tienda = Tienda.objects.get(id=id)
    tienda.nombre = nombre
    tienda.direccion = direccion
    tienda.telefono = telefono
    tienda.email = email
    tienda.fecha = fecha
    tienda.save()
    messages.success(request, "SE HA EDITADO LA TIENDA")

    return redirect('indexTienda')
