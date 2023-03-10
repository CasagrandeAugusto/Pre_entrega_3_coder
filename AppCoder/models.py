from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField
from distutils.command.upload import upload


# Create your models here.
class Producto(models.Model):
    nombreProducto= models.CharField(max_length=40)
    categoria= models.CharField(max_length=40)
    fechaingreso= models.DateField()
    costo= models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombreProducto} - Categoria: {self.categoria} - Fecha ingreso: {self.fechaingreso} - Costo: {self.costo} "

class Proveedor(models.Model):
    nombreP= models.CharField(max_length=40)
    apellidoP= models.CharField(max_length=40)
    telefonoP= models.IntegerField()
    direccionP=models.CharField(max_length=40)
    def __str__(self):
        return f"Nombre: {self.nombreP} - Apellido: {self.apellidoP} - Telefono: {self.telefonoP} - Direccion: {self.direccionP} "


class Destinatario(models.Model):
    nombreD= models.CharField(max_length=40)
    apellidoD= models.CharField(max_length=40)
    telefonoD= models.IntegerField()
    direccionD=models.CharField(max_length=40)
    def __str__(self):
        return f"Nombre: {self.nombreD} - Apellido: {self.apellidoD} - Telefono: {self.telefonoD} - Direccion: {self.direccionD} "

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares',null=True, blank = True)

   


