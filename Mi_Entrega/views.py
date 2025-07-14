from django.shortcuts import render, redirect

from .models import Producto, Cliente, Empleado

from .forms import FormsCliente, FormsEmpleados, FormsProducto
# Create your views here.

def Home(request):
    return render(request, "Mi_Entrega/Home.html")

def nuevoCliente(request):
    if request.method == "POST":
        form = FormsCliente(request.POST)
        if form.is_valid():
            newCliente = Cliente (
                nombre= form.cleaned_data["nombre"],
                apellido= form.cleaned_data["apellido"],
                edad= form.cleaned_data["edad"],
                email= form.cleaned_data["email"],
            )
            newCliente.save()
            return redirect("Inicio")
    else:
        form= FormsCliente
        return render(request, "Mi_Entrega/crear_Cliente.html", {"form": form})

def nuevoEmpleado(request):
    if request.method == "POST":
        form = FormsEmpleados(request.POST)
        if form.is_valid():
            newEmpleado = Empleado (
                nombre= form.cleaned_data["nombre"],
                apellido= form.cleaned_data["apellido"],
                edad= form.cleaned_data["edad"],
                email= form.cleaned_data["email"],
                Cuil= form.cleaned_data["Cuil"]
            )
            newEmpleado.save()
            return redirect("Inicio")
    else:
        form= FormsEmpleados
        return render(request, "Mi_Entrega/crear_Cliente.html", {"form": form})

def nuevoProducto(request):
    if request.method == "POST":
        form = FormsProducto(request.POST)
        if form.is_valid():
            newProducto = Producto (
                nombre= form.cleaned_data["nombre"],
                Tipo= form.cleaned_data["Tipo"],
                Marca= form.cleaned_data["Marca"]
            )
            newProducto.save()
            return redirect("Inicio")
    else:
        form= FormsProducto
        return render(request, "Mi_Entrega/crear_Cliente.html", {"form": form})
    
def producto(request):
    producto= Producto.objects.all()
    return render(request, "Mi_Entrega/buscar_Producto.html", {"producto": producto})

def buscar_Producto(request):
    if request.method == "GET":
        nombre= request.GET.get("nombre", "")
        producto= FormsProducto.objects.filter(nombre__icontains= nombre)
        return render(request, "Mi_Entrega/buscar_Producto.html", {"Producto": FormsProducto, "Nombre": producto})