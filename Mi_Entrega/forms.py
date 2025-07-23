from django import forms
from .models import Verduras

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

class FormsVerduras(forms.ModelForm):
    class Meta:
        model = Verduras
        fields = ['nombre', 'precio', 'cantidad']