from django.contrib import admin

# Register your models here.
from .models import Cliente, Producto, Empleado

register_models= [Cliente, Producto, Empleado]
admin.site.register(register_models)

