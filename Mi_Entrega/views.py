from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from .models import Producto, Cliente, Empleado, Verduras

from .forms import FormsCliente, FormsEmpleados, FormsProducto, FormsVerduras
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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
            form.save()
            return redirect("Inicio")
    else:
        form = FormsProducto()
    return render(request, "Mi_Entrega/crear_Producto.html", {"form": form})
    
def producto(request):
    productos = Producto.objects.all()
    return render(request, "Mi_Entrega/buscar_Producto.html", {"productos": productos})

def buscar_Producto(request):
    if request.method == 'GET':
        nombre = request.GET.get("nombre")
        if nombre:  # Solo busca si hay nombre
            producto = Producto.objects.filter(nombre__icontains=nombre)
            return render(request, "Mi_Entrega/buscar_Producto.html", {"producto": producto})
        else:
            return render(request, "Mi_Entrega/buscar_Producto.html", {"error": "Debes ingresar un nombre para buscar."})
    else:
        return render(request, "Mi_Entrega/buscar_Producto.html", {"error": "No se encontró el producto."})


class VerdurasListView(LoginRequiredMixin, ListView):
    model = Verduras
    template_name = 'Mi_Entrega/lista_verduras.html'
    context_object_name = 'verduras'


class VerdurasCreateView(LoginRequiredMixin, CreateView):
    model = Verduras
    form_class = FormsVerduras
    template_name = 'Mi_Entrega/hacer_verduras.html'
    success_url = reverse_lazy('lista-verduras')


class VerdurasUpdateView(LoginRequiredMixin, UpdateView):
    model = Verduras
    form_class = FormsVerduras
    template_name = 'Mi_Entrega/hacer_verduras.html'
    success_url = reverse_lazy('lista-verduras')


class VerdurasDeleteView(LoginRequiredMixin, DeleteView):
    model = Verduras
    template_name = 'Mi_Entrega/verduras_confirm_delete.html'
    success_url = reverse_lazy('lista-verduras')


class VerdurasDetailView(LoginRequiredMixin, DetailView):
    model = Verduras
    template_name = 'Mi_Entrega/verduras_detail.html'
    context_object_name = 'verdura'
    