from dataclasses import field
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoFormulario(forms.Form):
    nombreProducto= forms.CharField(max_length=40)
    categoria= forms.CharField(max_length=40)
    fechaingreso= forms.DateField()
    costo= forms.IntegerField()

class ProveedorFormulario(forms.Form):
    nombreP= forms.CharField(max_length=40)
    apellidoP= forms.CharField(max_length=40)
    telefonoP= forms.IntegerField()
    direccionP=forms.CharField(max_length=40)

class DestinatarioFormulario(forms.Form):
    nombreD= forms.CharField(max_length=40)
    apellidoD= forms.CharField(max_length=40)
    telefonoD= forms.IntegerField()
    direccionD=forms.CharField(max_length=40)
    

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):
   
    email = forms.EmailField(label="Modificar E-mail")
    password1= forms.CharField(label='Contraseña Antigua', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir la contraseña Antigua', widget=forms.PasswordInput)

    
    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}        