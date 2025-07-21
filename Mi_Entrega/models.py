from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre= models.CharField(max_length=50)
    Tipo= models.CharField(max_length=50)
    Marca= models.CharField(max_length=50)

def __str__(self):
    return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length= 50)
    apellido = models.CharField(max_length= 50)
    edad = models.IntegerField()
    email= models.CharField(max_length= 50)

def __str__(self):
    return f"{self.nombre} {self.apellido} - Edad: {self.edad} - Correro: {self.email}"

class Empleado(models.Model):
    nombre = models.CharField(max_length= 50)
    apellido = models.CharField(max_length= 50)
    edad = models.IntegerField()
    email= models.CharField(max_length= 50)
    Cuil= models.IntegerField()

def __str__(self):
    return f"{self.nombre} {self.apellido} - Edad: {self.edad} - Correro: {self.email} - CUIL: {self.Cuil}"