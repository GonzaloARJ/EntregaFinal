from django.urls import path
from .views import (nuevoProducto, nuevoCliente, Home,
                     nuevoEmpleado, buscar_Producto, producto,
                     VerdurasCreateView, VerdurasListView, VerdurasDetailView, VerdurasUpdateView, VerdurasDeleteView)

urlpatterns = [
    path("", Home, name="Inicio"),
    path("Crear-Empleado/", nuevoEmpleado, name="Crear-Empleado"),
    path("Crear-cliente/", nuevoCliente, name="Crear-Cliente"),
    path("Crear-Producto/", nuevoProducto, name="Crear-Producto"),
    path("Productos/", producto, name="Producto"),
    path("buscar-Producto/", buscar_Producto, name="buscar-Producto"),

    path("hacer-verduras/", VerdurasCreateView.as_view(), name="hacer-verduras"),
    path("lista-verduras/", VerdurasListView.as_view(), name="lista-verduras"),
    path("detalle-verduras/<int:pk>", VerdurasDetailView.as_view(), name="detalle-verduras"),
    path("borrar-verduras/<int:pk>", VerdurasDeleteView.as_view(), name="borrar-verduras"),
    path("editar-verduras/<int:pk>", VerdurasUpdateView.as_view(), name="editar-verduras"),
]