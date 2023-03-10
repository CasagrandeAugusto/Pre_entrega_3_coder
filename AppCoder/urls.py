from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',views.inicio,name='inicio'),
    #--------------producto-----------------------
    path('prod',views.producto,name='prod'),
    path('formularioprod',views.formularioprod,name='formularioprod'),
    path('leerprod',views.leerprod,name='leerprod'),
    path('eliminarprod/<prod_nombre>/',views.eliminarprod,name='eliminarprod'),
    path('editarprod/<prod_nombre>/',views.editarprod,name='editarprod'),
    path('busquedaprod',views.busquedaprod,name='busquedaprod'),
    path('buscar/',views.buscar),
    #--------------proveedor-----------------------
    path('proveedor',views.proveedor,name='proveedor'),
    path('formularioproveedor',views.formularioproveedor,name='formularioproveedor'),
    path('leerproveedor',views.leerproveedor,name='leerproveedor'), 
    path('eliminarproveedor/<proveedor_nombre>/',views.eliminarproveedor,name='eliminarproveedor'),
    path('editarproveedor/<proveedor_nombre>/',views.editarproveedor,name='editarproveedor'),

    #--------------Vetirinario-----------------------
    path('destinatario',views.destinatario,name='destinatario'),
    path('formulariodestinatario',views.formulariodestinatario,name='formulariodestinatario'),
    path('leerdestinatario',views.leerdestinatario,name='leerdestinatario'), 
    path('eliminarproveedor/<proveedor_nombre>/',views.eliminarproveedor,name='eliminarproveedor'),
    path('editarproveedor/<proveedor_nombre>/',views.editarproveedor,name='editarproveedor'),


    #--------------Loguin/Register--------------------
    path('login',views.login_request, name='Login'),
    path('register',views.register, name='Register'),
    path('logout',LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    
]