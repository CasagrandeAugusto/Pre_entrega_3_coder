from django.contrib import admin
from  .models import * #importamos el archivo models

# Register your models here.
#registramos los modelos

admin.site.register(Producto)

admin.site.register(Proveedor)

admin.site.register(Destinatario)

admin.site.register(Avatar)


