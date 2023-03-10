#---------prueba-----------#
from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import ProductoFormulario,ProveedorFormulario,UserRegisterForm,DestinatarioFormulario,UserEditForm
from AppCoder.models import Producto, Avatar,Proveedor,Destinatario
#CVB
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
#-Login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

#-----------------------------------------PRODUCTO-------------------------------------------------------
def producto(request):
    return render(request,"AppCoder/Producto.html")

@login_required
def leerprod(request):
    productos = Producto.objects.all()
    contexto = {"productos":productos}
    return render(request,"AppCoder/Producto.html",contexto)

def formularioprod(request):
    if request.method == 'POST':
        miFormulario = ProductoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
		    
            prod = Producto(nombreproducto=informacion['nombreProducto'],
            categoria=informacion['categoria'],
            fechaingreso=informacion['fecha'],
            costo=informacion['costo'])
		    
            prod.save()

            productos = Producto.objects.all()
    
            return render(request,"AppCoder/producto.html",{"productos":productos})

    else:
        miFormulario = ProductoFormulario()
    return render(request, "AppCoder/formularioprod.html",{"miFormulario":miFormulario})

def editarprod(request,prod_nombre):

    prod = Producto.objects.get(nombreproducto = prod_nombre)

    if request.method == 'POST':
        miFormularioprod = ProductoFormulario(request.POST)
        print(miFormularioprod)

        if miFormularioprod.is_valid:
            
            informacion = miFormularioprod.cleaned_data
		    
            prod.nombreProducto=informacion['nombreproducto']
            prod.categoria=informacion['categoria']
            prod.fechaingreso=informacion['fecha']
            prod.costo=informacion['costo']
		    
            prod.save()
            
            return render(request, "AppCoder/inicio.html")

    else:
        miFormularioprod= ProductoFormulario(initial={'nombreproducto': prod.nombreproducto, 'categoria':prod.categoria ,'fecha':prod.fechaingreso , 'costo':prod.costo }) 
    
    return render(request, "AppCoder/editarprod.html", {"miFormularioprod": miFormularioprod, "prod_nombre":prod_nombre})
        
def eliminarprod(request,prod_nombre):
    prod = Producto.objects.get(nombreproducto=prod_nombre)
    prod.delete()
    productos = Producto.objects.all()
    contexto ={"productos":productos}
    return render(request,"AppCoder/producto.html",contexto)

@login_required
def busquedaprod(request):
    return render(request,"AppCoder/busquedaProducto.html")
    
#@login_required
#def buscar(request):
        
    if request.GET["nombreProducto"]:
        nombreproducto = request.GET['nombreProducto']
        productos = Producto.objects.filter(nombreproducto__icontains=nombreproducto)
        
        return render(request, "AppCoder/Producto.html",{"productos":productos})

    else:
        respuesta = "No enviaste nada"
    return render(request,"AppCoder/inicio.html",{"respuesta":respuesta})

@login_required
def buscar(request):
    nombreproducto = request.GET.get('nombreProducto')
    
    if nombreproducto:
        productos = Producto.objects.filter(nombreproducto__icontains=nombreproducto)
        return render(request, "AppCoder/Producto.html", {"productos": productos})
    else:
        respuesta = "No enviaste nada"
        return render(request, "AppCoder/inicio.html", {"respuesta": respuesta})


#-----------------------------------------Proveedor-------------------------------------------------------
def proveedor(request):
    return render(request,"AppCoder/proveedor.html")

@login_required
def leerproveedor(request):
    proveedores = Proveedor.objects.all()
    contexto = {"proveedores":proveedores}
    return render(request,"AppCoder/proveedor.html",contexto)

def formularioproveedor(request):

    if request.method == 'POST':
        miFormularioproveedor = ProveedorFormulario(request.POST)
        print(miFormularioproveedor)

        if miFormularioproveedor.is_valid:
            
            informacion = miFormularioproveedor.cleaned_data
		    
            proveedor = Proveedor(nombreP=informacion['nombreP'],
            apellidoP=informacion['apellidoP'],telefonoP=informacion['telefonoP'],direccionP=informacion["direccionP"])
		    
            proveedor.save()

            proveedores = Proveedor.objects.all()
            
            return render(request,"AppCoder/Proveedor.html",{"proveedores":proveedores})

    else:
        miFormularioproveedor = ProveedorFormulario()
    return render(request, "AppCoder/formularioProveedor.html",{"miFormularioproveedor":miFormularioproveedor})

def editarproveedor(request,proveedor_nombre):

    proveedor = Proveedor.objects.get(nombre = proveedor_nombre)

    if request.method == 'POST':
        miFormularioproveedor = ProveedorFormulario(request.POST)
        print(miFormularioproveedor)

        if miFormularioproveedor.is_valid:
            
            informacion = miFormularioproveedor.cleaned_data
		    
            proveedor.nombreP=informacion['nombre']
            proveedor.apellidoP=informacion['apellido']
            proveedor.telefonoP=informacion['telefono']
            proveedor.direccionP=informacion['direccion']
		    
            proveedor.save()
            
            return render(request, "AppCoder/inicio.html")

    else:
        miFormularioproveedor= ProveedorFormulario(initial={'nombre': proveedor.nombre, 'apellido':proveedor.apellido , 
            'telefono':proveedor.telefono , "direccion":proveedor.direccion})
    
    return render(request, "AppCoder/editarproveedor.html", {"miFormularioproveedor": miFormularioproveedor, "proveedor_nombre":proveedor_nombre})
        
def eliminarproveedor(request,proveedor_nombre):
    proveedor = Proveedor.objects.get(nombre=proveedor_nombre)
    proveedor.delete()
    proveedores = Proveedor.objects.all()
    contexto ={"proveedores":proveedores}
    return render(request,"AppCoder/proveedor.html",contexto)

#-----------------------------------------destinatario-------------------------------------------------------
def destinatario(request):
    return render(request,"AppCoder/destinatario.html")

@login_required
def leerdestinatario(request):
    destinatarios = Destinatario.objects.all()
    contexto = {"destinatarios":destinatarios}
    return render(request,"AppCoder/destinatario.html",contexto)

def formulariodestinatario(request):

    if request.method == 'POST':
        miFormulariodestinatario = DestinatarioFormulario(request.POST)
        print(miFormulariodestinatario)

        if miFormulariodestinatario.is_valid:
            
            informacion = miFormulariodestinatario.cleaned_data
		    
            destinatario = Destinatario(nombreD=informacion['nombreD'],
            apellidoD=informacion['apellidoD'],telefonoD=informacion['telefonoD'],direccionD=informacion["direccionD"])
		    
            destinatario.save()

            destinatarios = Destinatario.objects.all()
            
            contexto = {"destinatarios":destinatarios}
            return render(request,"AppCoder/destinatario.html",contexto)

    else:
        miFormulariodestinatario = DestinatarioFormulario()
    return render(request, "AppCoder/formulariodestinatario.html",{"miFormulariodestinatario":miFormulariodestinatario})




#-----------------------------------------Loguin/Register-------------------------------------------------------
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario,password = contra)

            if user is not None:
                login(request,user)

                return render(request,"AppCoder/inicio.html",{"mensaje":f"Bienvenido {usuario}"})
            else:
                
                return render(request,"AppCoder/inicio.html",{"mensaje":"Error,datos incorrectos"})

        else:
            
                return render(request,"AppCoder/inicio.html",{"mensaje":"Error,formulario erroneo"})

    form = AuthenticationForm()

    return render(request,"AppCoder/login.html",{'form':form})


def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"AppCoder/inicio.html",{"mensaje":"Usuario Creado :)"})
    else:
        form = UserRegisterForm()
        #form = UserCreationForm()
    return render(request,"AppCoder/registro.html",{"form":form})


def inicio(request):
    return render(request,"AppCoder/inicio.html")

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1= informacion['password1']
            usuario.password2= informacion['password1']            
            usuario.save()
            

            return render(request, "AppCoder/inicio.html")
    else:

        miFormulario = UserEditForm(initial={'email':usuario.email})
    return render(request, "AppCoder/editarPerfil.html",{"miFormulario": miFormulario, "usuario":usuario})



#-----------------------------------------Avatar-------------------------------------------------------
@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)

    return render(request,"AppCoder/inicio.html", {"url":avatares[0].imagen.url})