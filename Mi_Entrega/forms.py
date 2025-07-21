from django import forms

class FormsProducto(forms.Form):
    nombre= forms.CharField()
    Tipo= forms.CharField()
    Marca= forms.CharField()

class FormsCliente(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    edad= forms.IntegerField()
    email= forms.CharField()

class FormsEmpleados(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    edad= forms.IntegerField()
    email= forms.CharField()
    Cuil= forms.IntegerField()