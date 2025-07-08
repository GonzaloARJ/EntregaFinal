from django.urls import path
from .views import nuevoProducto, nuevoCliente, Home, nuevoEmpleado, buscar_Producto

urlpatterns = [
    path("", Home, name= "Inicio"),
    path("Crear-Empleado/", nuevoEmpleado, name="Crear Empleado"),
    path("Crear-cliente/", nuevoCliente, name="Crear Cliente"),
    path("Crear-Producto/", nuevoProducto, name="Crear Producto"),
    path("Buscar-Producto/", buscar_Producto, name="Buscar Producto")
]